# node[0] = key
# node[1] = value
# node[2] = rank
# node[3] = children
# node[4] = marked
# node[5] = parent

# heap[0] = min root
# heap[1] = list of roots

def find_min(heap):
  return heap[0];

def smaller_key(node1, node2):
  if (node1[0] < node2[0]):
    return node1;
  else:
    return node2;

def bigger_key(node1, node2):
  if (node1[0] < node2[0]):
    return node2;
  else:
    return node1;

def merge(heap1, heap2):
  return [smaller_key(node1, node2)[0], heap1[1]+heap2[1]];

def insert(node, heap):
  return merge([node, [node]], heap);

def remove(node, heap):
  heap[1] = heap[1].remove(node);
  return heap;

def consolidate(heap):
  while True:
    counter = 0;
    for node1, node2 in heap[1]:
      if node1 != node2 & node1[2] == node2[2]:
        small_node = smaller_key(node1, node2);
        big_node = bigger_key(node1, node2);
        heap = remove(big_node, heap);
        small_node[2] = small_node[2] * 2;
        small_node[3] = small_node[3].append(big_node)
        counter = 1;
        break;
    if counter == 0:
      break;
  return heap;

def find_min(heap):
  min = heap[1][1];
  for node in heap[1]:
    min = smaller_key(min, node);
  return min

def extract_min(heap):    
  small_node = find_min(heap);
  heap = remove(small_node, heap);
  for node in small_node[3]:
    heap = insert(node, heap);
  heap = consolidate(heap);
  heap[0] = find_min(heap);
  return heap[0];  

def cut(node, heap):
  node[5][3].remove(node);
  if node[5][4]:
    node[5][4] = False;
    heap = cut(node[5], heap);
  else:
    node[5][4] = True;
  return heap;

def decrease_key(node, new_key, heap):
  node[0] = new_key;
  if node[5] != None & node[5][0] > new_key:
    heap = insert(node, heap);
    cut(node, heap);
  return heap;

def delete(node, heap):
  decrease_key(node, float('-inf'));
  extract_min(heap);
  return heap;
