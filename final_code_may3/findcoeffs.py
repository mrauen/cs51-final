import random
import math
import graph
from helpers import itemgraph

c1lower = 0.
c2lower = 0.
c1upper = 3.
c2upper = 3.
slopes = [None]*3 
points = [[None]*2]*4

def regression_eq(c1, c2, n, s):
  return pow(1./(1+c1*math.exp(-c2*n)),s)

def sum_of_the_squares(c1, c2):
  global itemgraph
  sum = 0
  for item in itemgraph.item_list:
    for edge in item.edge_list:
      sum += (edge.conf - regression_eq(c1, c2, edge.num_ratings, edge.stdev))**2
  return sum

def temperature(n):
  return math.sqrt(c1upper*c2upper)*(0.8 ** (n / 25000))

def dist(p1, p2):
  return abs(p1[0]-p2[0] + p1[1]- p2[1])

def SA_prob(old, new, n):
  return 1 / (1+math.exp((old - new)/temperature(n)))

def find_coeffs():
  global points
  global slopes
  correction_factor = 3
  x = 0.01
  c1 = random.uniform(c1lower, c1upper)
  c2 = random.uniform(c2lower, c2upper)
  M = sum_of_the_squares(c1, c2)
  current = M

  while points[0] == [None,None]:
    c1 = random.uniform(max(c1-x,c1lower),min(c1+x,c1upper))
    c2 = random.uniform(max(c2-x,c2lower),min(c2+x,c2upper))
    current = sum_of_the_squares(c1,c2)
    if(current < M):
      M = current
    slopes = [slopes[1],slopes[2], M - current]
    points = [points[1], points[2], points[3], (c1, c2)]

  for i in range(0,5000):
    if(slopes[0] > 0 and slopes[2] > 0):
      x += 0.01
      #max(dist(points[0],points[3]), dist(points[1],points[3]), dist(points[2], points[3]))
    elif (slopes[0] < 0 and slopes[2] > 0):
      c1 = points[2][0]
      c2 = points[2][1]
      x /= correction_factor
    new_c1 = random.uniform(max(c1-x,c1lower),min(c1+x,c1upper))
    new_c2 = random.uniform(max(c2-x,c2lower),min(c2+x,c2upper))
    new_M = sum_of_the_squares(new_c1,new_c2)
    if(new_M < current):
      c1 = new_c1
      c2 = new_c2
      current = new_M
      M = min(M, current)
      slopes = [slopes[1],slopes[2], new_M - current]
      points = [points[1], points[2], points[3], (c1, c2)]
    elif (new_M >= current and random.random() < SA_prob(current, M, i)):
      c1 = new_c1
      c2 = new_c2
      current = M
      slopes = [slopes[1],slopes[2], new_M - current]
      points = [points[1], points[2], points[3], (c1, c2)]
  #return M/2 to correct for double counting
  return (c1, c2, (M/2))
