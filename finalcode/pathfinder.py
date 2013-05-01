# Pathfinder.py
# Contains modified Dijkstra algorithm to be used in Graph.
import random
import sys
import fileinput
import fibonacciheap
import graph

def pathfinder (self, item_id, useritem_ids):
  dist = {item_id : 0}
  prev = {}
  Q = fibonacciheap.empty_heap
  fibonacciheap.insert_new_pair(item_id, 0, Q)
  for v in self.item_list:
    dist[v.id] = -1
    prev[v.id] = None
  iterator = start
  while(fibonacciheap.is_empty(Q)):
    u = fibonacciheap.extract_min(Q)
    if dist[u.id] == -1:
      break
    for edge in u.edge_list:
      alt = dist[u.id] + math.log(edge.conf)
      if alt < dist[edge.neighbor_id]:
        dist[edge.neighbor_id] = alt
        prev[edge.neighbor_id] = u;
        fibonacciheap.insert_new_pair(edge.neighbor_id, dist[edge.neighbor_id],Q)
  M = 0
  candidate = useritem_ids[0]
  for item in useritem_ids:
    if(dist[item] > M):
      M = dist[item]
      candidate = item
  cursor = prev[candidate]
  diff = 0
  while(cursor2 != item):
    tmp = prev[cursor]
    info = get_edge(tmp,cursor)
    diff += info[0]*info[1]
    cursor = item[prev]
  return (math.exp(M), diff)

if(len(sys.argv) != 2):
  print "Usage: file"
else:
  f = open(sys.argv[1], 'r')
  N = int(float(f.readline()))
  vs = []
  for n in range(0,N):
    vs.append(graph.Item(n,0,"",0,0,{}))
  counter = 0
  while True:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    if not line2 or not line3: break
    edges = line1.split()
    confs = line2.split()
    diffs = line3.split()
    nums = line4.split()
    n = len(edges)
    for i in range(0,n):
      conf = int(float(confs[i]))
      diff = int(float(diffs[i]))
      num = int(float(nums[i]))
      edge = int(float(edges[i]))
      e = graph.Edge(vs[edge], None, diff, 0, num, conf)
      vs[i].edge_list.append(e)
  g = graph.Graph("test", vs)
  answer = pathfinder(g, vs[0], [vs[3]])
  print(answer)