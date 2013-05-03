# node[0] = key
# node[1] = value
# node[2] = rank
# node[3] = children
# node[4] = marked
# node[5] = parent

# heap[0] = min root
# heap[1] = list of roots

import itertools

def empty_heap():
  return [None, []]

def is_empty(heap):
  return heap[1] == []

def insert_new_pair(key, value, heap):
   return insert([key, value, 1, [], False, None], heap)

def find_min(heap):
  return heap[0];

def smaller_key(node1, node2):
  if node2 == None:
    return node1
  elif node1[1] < node2[1]:
    return node1;
  else:
    return node2;

def bigger_key(node1, node2):
  if node2[1] == None:
    return node1;
  if (node1[1] < node2[1]):
    return node2;
  else:
    return node1;

def merge(heap1, heap2):
  return [smaller_key(heap1[0], heap2[0]), heap1[1]+heap2[1]]; 

def insert(node, heap):
  return merge([node, [node]], heap);

def remove(node, heap):
  copy_of_heap = heap
  copy_of_heap[1].remove(node);
  return copy_of_heap;

def consolidate(heap):
  while True:
    counter = 0;
    if len(heap[1]) > 1:
      for node1, node2 in itertools.product(heap[1], repeat=2):
        if node1 != node2 and node1[2] == node2[2]:
          small_node = smaller_key(node1, node2);
          big_node = bigger_key(node1, node2);
          heap = remove(big_node, heap);
          small_node[2] = small_node[2] * 2;
          # My addition
          small_node[3] += [big_node]
          big_node[5] = small_node;
          counter = 1;
          break;
    if counter == 0:
      break;
  return heap;

def find_new_min(heap):
  if heap[1] == []:
    return None;
  else:
    min = heap[1][0];
    for node in heap[1]:
      min = smaller_key(min, node);
    return min

def extract_min(heap):    
  small_node = find_min(heap);
  heap = remove(small_node, heap);
  if small_node[3] != []: 
    for node in small_node[3]:
      heap = insert(node, heap);
  heap = consolidate(heap);
  heap[0] = find_new_min(heap);
  return [small_node[0], small_node[1], heap];  

def cut(node, heap):
  parent_node = node[5];
  parent_node[3].remove(node);
  parent_node[2] = parent_node[2] - node[2];
  if parent_node[4] and parent_node[5] != None:
    parent_node[4] = False;
    node[5] = None;
    heap = cut(parent_node, heap);
  else:
    parent_node[4] = True;
  heap = insert(node, heap);
  return heap;

def decrease_key(node, new_key, heap):
  node[0] = new_key;
  if node[5] != None and node[5][0] > new_key:
    cut(node, heap);
  return heap;

def delete(node, heap):
  decrease_key(node, float('-inf'));
  extract_min(heap);
  return heap;