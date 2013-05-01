# Pathfinder.py
# Contains modified Dijkstra algorithm to be used in Graph.
import random
import sys
import fileinput
import fibonacciheap

def pathfinder (self, item_id, useritem_ids):
  dist = {item : 0}
  prev = {}
  Q = fibonacciheap.empty_heap
  fibonacciheap.insert_new_pair(item, 0, Q)
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
  N = int(float(sys.stdin.readline()))
  for n in range(0,N):
    vs.append(Item(n,0,"",0,0,{}))
  counter = 0
  while True:
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    line3 = sys.stdin.readline()
    line4 = sys.stdin.readline()
    if not line2 || not line3: break
    edges = line1.split()
    confs = line2.split()
    diffs = line3.split()
    nums = line4.split()
    n = len(edges)
    for i in range(0,n):
      conf = confs[i]
      diff = diffs[i]
      num = nums[i]
      edge = edge[i]
      e = Edge(vs[edge], None, diff, 0, num, conf)
      vs[i].edge_list.append(e)
  g = Graph("test", vs)
  answer = graph.findpath(g, vs[0], [vs[3]]))
  print(answer)