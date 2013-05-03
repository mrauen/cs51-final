# Graph.py
# Contains type definitions for graph and nodes, and methods for traversing, updating, and deleting. 
# Also contains brand graph and item graph.

# prediction_list: a list of (user ID, number of edges in path, prediction)
# items in prediction_list have not been rated

    
class Edge:
  def __init__ (self, neighbor_pointer = None, list_of_diffs = None, mean_of_diffs = None, stdev = None, num_ratings = None, conf = None, scaling_factor = None):
    if neighbor_pointer is None:
      neighbor_pointer = None
    if list_of_diffs is None:
      list_of_diffs = []
    if mean_of_diffs is None:
      mean_of_diffs = None
    if stdev is None:
      stdev = None
    if num_ratings is None:
      num_ratings = 0
    if conf is None:  
      conf = 0
    if scaling_factor is None:
      scaling_factor = None
    self.neighbor_pointer = neighbor_pointer
    self.list_of_diffs = list_of_diffs
    self.mean_of_diffs = mean_of_diffs
    self.stdev = stdev
    self.num_ratings = num_ratings
    self.conf = conf
    self.scaling_factor = scaling_factor


# items come from a Mysql database of all possible items, that contains these fields (including is_new which gets changed to false when item is purchased)    
class Item:
  def __init__ (self, id = None, name = None, brandname = None, nom_size = None, act_size = None, num_ratings = None, avg_rating = None, edge_list = None, is_new = None) :
    if id is None:  
      id = -1
    if name is None:
      name = ""  
    if brandname is None:
      brandname = ""
    if nom_size is None:
      nom_size = None
    if act_size is None:
      act_size = None
    if num_ratings is None:
      num_ratings = 0
    if avg_rating is None:
      avg_rating = None
    if edge_list is None:
      edge_list = []
    if is_new is None:
      is_new = True  
    self.id = id
    self.name = name
    self.brandname = brandname
    self.nom_size = nom_size
    self.act_size = act_size
    self.num_ratings = num_ratings
    self.avg_rating = avg_rating
    self.edge_list = edge_list
    self.is_new = is_new  
  def neighbors_list (self):
    return [x.neighbor_pointer for x in self.edge_list]


class Brand:
  def __init__ (self, id = None, name = None, edge_list = None, item_list = None) :
    if id is None:
      id = None
    if name is None:
      name = ""
    if edge_list is None:
      edge_list = []
    if item_list is None:
      item_list = []
    self.id = id
    self.name = name
    self.edge_list = edge_list
    self.item_list = item_list
  def neighbors_list (self):
    return [x.neighbor_pointer for x in self.edge_list]
    
class Graph:
  def __init__ (self, name = None, item_list = None): # this is where Item() and Brand() would go
    if name is None:
      name  = ""
    if item_list is None:
      item_list = []
    self.name = name
    self.item_list = item_list  
  def itemid_list (self):
    return [x.id for x in self.item_list]
  def brand_list (self):
    return [x.name for x in self.item_list]    
  def empty_graph (self):
    self.item_list = []


class User:
  def __init__ (self, name = None, id = None, itemrating_list = None, size = None):
    if name is None:
      name = ""
    if id is None:
      id = -1 
    if itemrating_list is None:
      itemrating_list = []
    if size is None:
      size = 30
    self.name = name
    self.id = id
    self.itemrating_list = itemrating_list
    self.size = size