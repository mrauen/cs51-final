# Pathfinder.py
# Contains modified Dijkstra algorithm to be used in Graph.
import random
import sys
import fileinput
import fibonacciheap
import graph
import math
import helpers
from helpers import itemgraph, brandgraph

def get_edge(start, end):
  for edge in start.edge_list:
    if edge.neighbor_pointer == end:
      return edge.mean_of_diffs

  return None

def pathfinder (item, user):
  global itemgraph
  global brandgraph
  dist = {}
  Q = fibonacciheap.empty_heap()
  Q=fibonacciheap.insert_new_pair((item,0), 0, Q)
  for v in itemgraph.item_list:
    dist[v] = sys.maxint
  dist[item] = 0
  found = False
  # virtual_best stores as (key, value) the best (conf, diff)
  virtual_best = [sys.maxint, 0, None]
  while(not fibonacciheap.is_empty(Q)):
    result = fibonacciheap.extract_min(Q)
    key = result[0]
    Q = result[2]
    u = key[0]
    diff = key[1]
    if dist[u] == sys.maxint:
      break
    if u in [x[0] for x in user.itemrating_list]:
      target_rating = user.itemrating_list[[x[0] for x in user.itemrating_list].index(u)]
      return(math.exp(-dist[u]), diff+target_rating[1])
    for edge in u.edge_list:
      if (edge.conf != 0):
        alt = dist[u] - math.log(edge.conf)
        newdiff = diff + edge.mean_of_diffs
        if alt < dist[edge.neighbor_pointer]:
          dist[edge.neighbor_pointer] = alt
          Q = fibonacciheap.insert_new_pair([edge.neighbor_pointer,newdiff], dist[edge.neighbor_pointer],Q)
      else:
        for i in [x[0] for x in user.itemrating_list]:
          u_brand = helpers.get_brand_from_name(u.brandname)
          i_brand = helpers.get_brand_from_name(i.brandname)
          if (i_brand != u_brand) and (i_brand in u_brand.neighbors_list()):
            edge = u_brand.edge_list[u_brand.neighbors_list().index(i_brand)]
            if(edge.conf != 0):
              alt = dist[u] - math.log(edge.conf)
              if alt < virtual_best[0]:
                virtual_best[0] = alt
                virtual_best[1] = diff + edge.mean_of_diffs
                virtual_best[2] = i
  target_rating = user.itemrating_list[[x[0] for x in user.itemrating_list].index(virtual_best[2])]
  return (math.exp(-virtual_best[0]), virtual_best[1] + target_rating[1])

# if(len(sys.argv) != 2):
#   print "Usage: file"
# else:
#   f = open(sys.argv[1], 'r')
#   N = int(float(f.readline()))
#   vs = []
#   for n in range(0,N):
#     new = graph.Item(n)
#     vs.append(new)
#   counter = 0
#   while True:
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()
#     if not line2 or not line3: break
#     edges = line1.split()
#     confs = line2.split()
#     diffs = line3.split()
#     n = len(edges)
#     for i in range(0,n):
#       conf = float(confs[i])
#       diff = int(float(diffs[i]))
#       edge = int(float(edges[i]))
#       e = graph.Edge(vs[edge], None, diff, 0, 0, conf, None)
#       vs[counter].edge_list.append(e)
#     counter += 1
#   g = graph.Graph("test", vs)
#   answer = pathfinder(g, vs[0], [vs[3]])
#   print(answer)