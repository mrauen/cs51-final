# Pathfinder.py
# Contains modified Dijkstra algorithm to be used in Graph.
import random
import sys
import fileinput

def pathfinder (self, item, useritems):
  dist = {item : 0}
  prev = {}
  Q = Heap(item : 0)
  for v in self.item_list:
    dist[v] = -1
    prev[v] = None
  iterator = start
  while(!Q.empty())
    u = Q.pop()
    if dist[u] == -1:
      break
    for edge in u.edge_list:
      alt = dist[u] + edge.conf
      if alt < dist[edge.neighbor_pointer]:
        dist[edge.neighbor_pointer] = alt
        prev[edge.neighbor_pointer] = u;
        Q.insert(edge.neighbor_pointer, dist[edge.neighbor_pointer])
  M = 0
  candidate = useritems[0]
  for item in useritems:
    if(dist[item] > M):
      M = dist[item]
      candidate = item
  cursor = prev[candidate]
  diff = 0
  ratings = 0
  while(cursor2 != item):
    tmp = prev[cursor]
    info = getEdge(tmp,cursor)
    diff += info[0]*info[1]
    ratings += info[1]
    cursor = item[prev]
  return (M, diff / ratings)

if(len(sys.argv) != 2):
  print "Usage: file"
else:
  n = int(float(sys.stdin.readline()))
  for n in range(0,N):
    vs.append(Item(n,0,"",0,0,{}))
  counter = 0
  while True:
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    line3 = sys.stdin.readline()
    if not line2 || not line3: break
    edges = line1.split()
    confs = line2.split()
    diffs = line3.split()
    n = len(edges)
    for i in range(0,n):
      conf = confs[i]
      diff = diffs[i]
      edge = edge[i]
      e = Edge(vs[edge], diff, 0, 0, conf, Ratings({},0,0))
      vs[i].edge_list.append(e)
  g = Graph("test", vs)
  answer = pathfinder(g, answer = pathfinder(g, vs[0], [vs[3]]))
