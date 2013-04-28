# Graph.py
# Contains type definitions for graph and nodes, and methods for traversing, updating, and deleting. 
# Also contains brand graph and item graph.

# prediction_list: a list of (user ID, number of edges in path, prediction)
# items in prediction_list have not been rated

    
class Edge:
	def __init__ (self, neighbor_id = None, list_of_diffs = None, mean_of_diffs = None, stdev = None, num_ratings = None, conf = None):
		if neighbor_pointer is None:
			neighbor_pointer = None
		if list_of_diffs is None:
			list_of_diffs = []
		if mean_of_diffs is None:
			mean_of_diffs = -1
		if stdev is None:
			stdev = None
		if num_ratings is None:
			num_ratings = 0
		if conf is None:	
			conf = 0
		self.neighbor_id = neighbor_id
		self.list_of_diffs = list_of_diffs
		self.mean_of_diffs = mean_of_diffs
		self.stdev = stdev
		self.num_ratings = num_ratings
		self.conf = conf


# items come from a Mysql database of all possible items, that contains these fields (including is_new which gets changed to false when item is purchased)		
class Item:
	def __init__ (self, id = None, name = None, brand = None, nom_size = None, act_size = None, num_ratings = None, avg_rating = None, edge_list = None, is_new = None) :
		if id is None:	
			id = -1
		if name is None:
			name = ""	
		if brand is None:
			brand = ""
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
		self.brand = brand
		self.nom_size = nom_size
		self.act_size = act_size
		self.num_ratings = num_ratings
		self.avg_rating = avg_rating
		self.edge_list = edge_list
		self.is_new = is_new
		self.neighbors_list = [x[0] for x in self.edge_list]
		
##class Brand:
##	def __init__ (self, id = -1, brand = "", nom_size = 0, act_size = 0, edge_list = {}, item_list = {} ) :
##                self.id = id

class Graph:
	def __init__ (self, name = None, item_list = None): # this is where Item() would go
		if name is None:
			name  = ""
		if item_list is None:
			item_list = []
		self.name = name
		self.item_list = item_list
		self.itemid_list = [x[0] for x in self.item_list]
	def empty_graph (self):
		self.item_list = []
	# check if item is in graph	

	def findpath (G, start, end):
		pathfinder(G, start, end) # defined in Pathfinder

		
class User:
	def __init__ (self, name = None, id = None, itemrating_list = None):
		if name is None:
			name = ""
		if id is None:
			id = -1 
		if itemrating_list is None:
			itemrating_list = []
		self.name = name
		self.id = id
		self.itemrating_list = itemrating_list
		
