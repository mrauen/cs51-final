# Pathfinder.py
# Contains modified Dijkstra algorithm to be used in Graph.
import random
import sys
import fileinput
import fibonacciheap
import graph

def pathfinder (self, item, useritem_ids):
  dist = {}
  prev = {}
  Q = fibonacciheap.empty_heap()
  Q=fibonacciheap.insert_new_pair(item, 0, Q)
  for v in self.item_list:
    dist[v] = 1000000
    prev[v] = None
  dist[item] = 0
  while(not fibonacciheap.is_empty(Q)):
    u = fibonacciheap.extract_min(Q)
    if dist[u[1]] == 1000000:
      break
    for edge in u.edge_list:
      alt = dist[u.id] + math.log(edge.conf)
      if alt < dist[edge.neighbor_id]:

        dist[edge.neighbor_id] = alt
        prev[edge.neighbor_id] = u.id;
        Q = fibonacciheap.insert_new_pair(edge.neighbor_id, dist[edge.neighbor_id],Q)
  M = 0
  candidate = useritem_ids[0].id
  for item in useritem_ids:
    if(dist[item.id] > M):
      M = dist[item.id]
      candidate = item.id
  cursor = prev[candidate]
  diff = 0
  while(cursor != item.id):
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
  for n in range(1,N+1):
    vs.append(graph.Item(n,"","",0,0,0,0,[],False))
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
  answer = pathfinder(g, vs[0].id, [vs[3]])
  print(answer)