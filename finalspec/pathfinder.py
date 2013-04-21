# Pathfinder.py
# Contains modified Dijkstra algorithm to be used in Graph.

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

vs = []
for n in range(0,n):
        vs.append(Item(n,0,"",0,0,{}))
for v in vs:
        for k in range(0,n):
                v.edge_list
