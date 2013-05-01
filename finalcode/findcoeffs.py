import random
import math
import graph

def regression_eq(c1, c2, n, s):
  return (1/(1+c_1*e**(-c2*n)))**s

def sum_of_the_squares(c1, c2):
  sum = 0
  for item in self.item_list:
    for edge in item.edge_list:
      sum += (edge.conf - regression_eq(c1, c2, edge.num_ratings, edge.stdev))**2
  return sum

def temperature(n):
  return math.sqrt(c1upper, c2upper)*(0.8 ** math.floor(n / 1000))

def dist(p1, p2):
  return math.abs(p1[0]-p2[0] + p1[1]- p2[1])

def SA_prob(old, new, n):
  return 1 / (1+pow((old - new)/temperature(n)))

def update(arr, n):
  slopes[0],slopes[1],slopes[2] = slopes[1],slopes[2],n

def find_coeffs():
  correction_factor = 3

  x = 0.01
  c1 = random.randrange(c1lower, c1upper)
  c2 = random.randrange(c2lower, c2upper)
  M = sum_of_the_squares(c1, c2)
  current = M

  slopes = [None]*3
  points = [(None)*2]*4

  while slopes[3] == None:
    new_c1 = random.randrange(max(c1-x,c1lower),min(c1+x,c1upper))
    new_c2 = random.randrange(max(c2-x,c2lower),min(c2+x,c2upper))
    new_M = sum_of_the_squares(c1,c2)
    if(new_M < current):
      c1 = new_c1
      c2 = new_c2
      M = new_M
      current = M
      update(slopes, new_M - current)
      update(points, (c1,c2))
    elif (new_M > M and random.random() < SA_prob(current, new_M, i)):
      c1 = new_c1
      c2 = new_c2
      current = M
      update(slopes, new_M - current)
      update(points, (c1,c2))

  for i in range(0,100000000):
    if(slopes[0] > 0 and slopes[2] > 0):
      x += max(dist(points[0],points[3]), dist(points[1],points[3]), dist(points[2], points[3]))
    elif (slopes[0] < 0 and slopes[2] > 0):
      c1 = points[2][0]
      c2 = points[2][1]
      x /= correction_factor
    new_c1 = random.randrange(c1-x,c1+x)
    new_c2 = random.randrange(c2-x,c2+x)
    new_M = sum_of_the_squares(c1,c2)
    if(new_M < current):
      c1 = new_c1
      c2 = new_c2
      M = new_M
      current = M
      update(slopes, new_M - current)
      update(points, (c1,c2))
    elif (new_M > M and random.random() < SA_prob(current, new_M, i)):
      c1 = new_c1
      c2 = new_c2
      current = M
      update(slopes, new_M - current)
      update(points, (c1,c2))
