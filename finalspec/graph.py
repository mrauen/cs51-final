# Graph.py
# Contains type definitions for graph and nodes, and methods for traversing, updating, and deleting. 
# Also contains brand graph and item graph.

import helpers
import pathfinder

# prediction_list: a list of (user ID, number of edges in path, prediction)
# items in prediction_list have not been rated
class Ratings:
  def __init__ (self, prediction_list = {}, tot_rated = 0, successes = 0):
  	self.prediction_list = prediction_list
  	self.tot_rated = tot_rated
  	self.successes = successes
  	
class Edge:
  def __init__ (self, neighbor_pointer = None, diff_mean = 0, stdev = 0, num_ratings = 0, conf = 0, ratings = Ratings):
	self.neighbor_pointer = neighbor_pointer
	self.diff_mean = diff_mean
	self.stdev = stdev
	self.num_ratings = num_ratings
	self.conf = conf
	self.ratings = ratings
	self.scaling_factor = scaling_factor #for brands, not accessed in item
	
class Item:
	def __init__ (self, id = 0, brand = "", nom_size = 0, act_size = 0,
		edge_list = {} ) : # this is where Edge() would go
	self.id = id
	self.brand = brand
	self.nom_size = nom_size
	self.act_size = act_size
	self.edge_list = edge_list
	
class Brand:
	def __init__ (self, id = 0, brand = "", nom_size = 0, act_size = 0,
		edge_list = {}, item_list = {} ) : # this is where Edge() would go
	self.id = id
	
class Graph:
	def __init__ (self, name = "", item_list = {}): # this is where Item() would go
		self.name = name
		self.item_list = item_list
	def empty_graph (self):
		self.item_list = {}
	# check if item is in graph	
	def in_graph (self, item):
		for node in self.item_list 
			if node.id == item.id: 
				return True
		else return False
	
	def getEdge (a, b):
		for edge in a.edge_list:
			if edge.neighbor_pointer = b:
				return (edge.ratings,edge.num_ratings)

	def insert (self, item, user):
		# if item is not in list of items in graph then add to the list
		if in_graph (self, item) == False:
			self.item_list.append(item) 
			# and 1- update the empty edge_list so that it 
			# 		 contains edges pointing to all items of the user,
			# and 2- update all items pointed to in each edge so that they
			# 	  	 contain an extra edge pointing to the new item
		else # find item in self.item_list and update graph in the same way as case directly above	
			
	
	def findpath (G, start, end):
		pathfinder(G, start, end) # defined in Pathfinder
		
	def predictor (path):	# path comes from another module where Dijkstra's or the fip heap is done
		# (Sigma diff_mean*num_ratings) / Sigma num_ratings

	def edge_update (self, edge):
		update # defined in helpers


