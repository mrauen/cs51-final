# Recommendations
import random
import sys
import fileinput
import fibonacciheap
import graph
import math
from helpers import users_list, items_list, itemgraph, brandgraph
 
def recommendations (user, num_items):
  global itemgraph
  dist = {}
  paths = []
  path_count = 0
  good_path = False
  best_val = 1000000
  Q = fibonacciheap.empty_heap()
  for v in itemgraph.item_list:
    dist[v] = 1000000
  for item in user.itemrating_list:
    Q = fibonacciheap.insert_new_pair([item[0],item[1]], 0, Q)
    dist[item[0]] = 0
  while(not fibonacciheap.is_empty(Q)):
    x = fibonacciheap.extract_min(Q)
    Q = x[2]    
    u = x[0][0]
    if (u not in [a[0] for a in user.itemrating_list]):
      if abs(x[0][1] - 50) <= 1:
        best_val = 1
        if good_path:
          new_path = True    
          for endpoints in paths:
            if endpoints[0] == u:
              new_path = False
          if new_path:
            paths += [[u,math.exp(-x[1]),x[0][1]]]
            path_count += 1
          if path_count >= num_items:
            break
        else:
          good_path = True
          paths = [[u,math.exp(-x[1]),x[0][1]]]
      elif paths == []:
        paths = [[u,math.exp(-x[1]),x[0][1]]]
        best_val = x[0][1] - 50
      elif abs(x[0][1] - 50) < abs(best_val):
        best_val = x[0][1] - 50
        paths = [[u,math.exp(-x[1]), x[0][1]]]
    if dist[u] == 1000000:
      break
    for edge in u.edge_list:
      if (edge.conf != 0):
        alt = dist[u] - math.log(edge.conf)
        if alt < dist[edge.neighbor_pointer]:
          dist[edge.neighbor_pointer] = alt
          Q = fibonacciheap.insert_new_pair([edge.neighbor_pointer, x[0][1]+edge.mean_of_diffs], dist[edge.neighbor_pointer], Q)
  return paths