#Helpers.py
import graph
import interval
import math
#Global Variables
itemgraph = graph.Graph()
brandgraph = graph.Graph()
items_list = []
users_list = []
current_user_id = 0
current_item_id = 0
current_brand_id = 0
num_items = 0
num_edges = 0
num_ratings = 0
edges_item = 0
ratings_item = 0
num_brands = 0

import pathfinder

def edges_per_item (num_items, num_edges):
    if num_items != 0 :
        return num_edges/num_items
    else:
        print ('No Items')

def ratings_per_item (num_items, num_edges):
    if num_items != 0 :
        return num_edges/num_items
    else:
        print "No Items"

#def get_item_from_id (itemgraph, id):
#  itemgraph.itemlist[itemgraph.(itemid_list ()).index (id)]

def get_brand_from_name (name):
  global brandgraph
  return brandgraph.item_list[brandgraph.brand_list().index (name)]

# Creates new user in users_list, each user has an id and a list of items he has purchased
def create_user (user):
  global users_list
  global current_user_id
  user.id = current_user_id
  users_list.append (user)
  current_user_id += 1

# updates users_list when user purchases item  
def update_user (userid, item, rating):
  global users_list
  users_list[userid].itemrating_list.append (item, rating) 

def new_item (item):
  global itemgraph  
  global current_item_id
  item.id = current_item_id
  current_item_id += 1
  item.is_new = False
  itemgraph.item_list.append (item)

def update_mean_stdev(m, std, n, x):
  newm = (m*n + x)/(n+1)
  diff = (newm - m)*(newm - m)*n+(x-newm)*(x-newm)
  newstd = math.sqrt((std * std * n + diff)/(n+1))
  return (newm, newstd)
  
  
def update_new_item (item, userid, rating):
  global users_list
  if users_list[userid].itemrating_list == []:
    pass
  else:  
    for (neighbor_item, neighbor_rating) in users_list[userid].itemrating_list:
      if (neighbor_item != item):
        edge = graph.Edge ()
        edge.neighbor_pointer = neighbor_item
        edge.list_of_diffs.append (rating - neighbor_rating)
        edge.num_ratings += 1
        edge.mean_of_diffs =  sum (edge.list_of_diffs) / edge.num_ratings
        edge.stdev = 0
        edge.conf = interval.conf(edge.list_of_diffs)
        item.edge_list.append (edge)

def update_user_items_new (item, userid, rating):
    global users_list
    global itemgraph
    if users_list[userid].itemrating_list == []:
            pass
    else:  
            for (neighbor_item, neighbor_rating) in users_list[userid].itemrating_list:
                    if neighbor_item == item:
                            pass
                    else:                             
                            edge = graph.Edge ()
                            edge.neighbor_pointer = item
                            edge.list_of_diffs.append (neighbor_rating - rating)
                            edge.num_ratings += 1
                            edge.mean_of_diffs =  sum (edge.list_of_diffs) / edge.num_ratings
                            edge.stdev = 0
                            edge.conf = interval.conf(edge.list_of_diffs)
                            neighbor_item.edge_list.append (edge)  

def update_existing_item (item, userid, rating):
  global users_list
  if users_list[userid].itemrating_list == []:
    pass
  else:  
    for (neighbor_item, neighbor_rating) in users_list[userid].itemrating_list:
      if neighbor_item in item.neighbors_list():
        edge = item.edge_list[item.neighbors_list().index (neighbor_item)]
        edge.list_of_diffs.append (rating - neighbor_rating)
        edge.num_ratings += 1
        (edge.mean_of_diffs, edge.stdev) = update_mean_stdev(edge.mean_of_diffs, edge.stdev, edge.num_ratings, (rating - neighbor_rating))
        edge.conf = interval.conf(edge.list_of_diffs)
        item.edge_list[item.neighbors_list().index (neighbor_item)] = edge
      else:
        edge = graph.Edge () 
        edge.neighbor_pointer = neighbor_item
        edge.list_of_diffs.append (rating - neighbor_rating)
        edge.num_ratings += 1
        edge.mean_of_diffs =  sum (edge.list_of_diffs) / edge.num_ratings
        edge.stdev = 0
        edge.conf = interval.conf(edge.list_of_diffs)
        neighbor_item.edge_list.append (edge)

def update_user_items_existing (item, userid, rating):
  global users_list
  global itemgraph
  if users_list[userid].itemrating_list == []:
    pass
  else:
    for (neighbor_item, neighbor_rating) in users_list[userid].itemrating_list:
      if neighbor_item == item:
        pass
      else:  
        if item in neighbor_item.neighbors_list():
          edge = neighbor_item.edge_list[neighbor_item.neighbors_list().index (item)]
          edge.list_of_diffs.append (neighbor_rating - rating)
          edge.num_ratings += 1
          (edge.mean_of_diffs, edge.stdev) = update_mean_stdev(edge.mean_of_diffs, edge.stdev, edge.num_ratings, (rating - neighbor_rating))
          edge.conf = interval.conf(edge.list_of_diffs)
          neighbor_item.edge_list[neighbor_item.neighbors_list().index (item)] = edge
        else:
          edge = graph.Edge ()
          edge.neighbor_pointer = item
          edge.list_of_diffs.append (neighbor_rating - rating)
          edge.num_ratings += 1
          edge.mean_of_diffs =  sum (edge.list_of_diffs) / edge.num_ratings
          edge.stdev = 0
          edge.conf = interval.conf(edge.list_of_diffs)
          neighbor_item.edge_list.append (edge)


def update_scale(n, sf, an, ar, bn, br):
       return (n*sf + (an*br/(bn*br)))/(n+1)


def new_brand (item, rating):  
  global current_brand_id
  global brandgraph
  newbrand = graph.Brand()
  newbrand.id = current_brand_id
  current_brand_id += 1
  newbrand.name = item.brandname
  brandgraph.item_list.append (newbrand)
  
'''def update_current_brand (brandgraph, brand, userid, item, rating):
  for (neighbor_item, neighbor_rating) in users_list[userid].itemrating_list:
    neighbor_brand = get_brand_from_name (brandgraph, neighbor_item.brandname)
    if neighbor_brand = brand:
      pass
    else: # if brand user owns is not the brand he's currently buying
      if neighbor_brand not in brand.neighbors_list(): # if brands are not connected yet
'''            
    
def update_brands (userid, item, rating):
  global users_list
  global brandgraph
  brand = get_brand_from_name (item.brandname)
  brand.item_list.append (item)  
  for (neighbor_item, neighbor_rating) in users_list[userid].itemrating_list:
    neighbor_brand = get_brand_from_name (neighbor_item.brandname)
    if neighbor_brand == brand:
      pass
    else: # if brand user owns is not the brand he's currently buying
      if neighbor_brand not in brand.neighbors_list(): # if brands are not connected yet
        new_edge = graph.Edge ()
        new_edge.neighbor_pointer = neighbor_brand
        new_edge.list_of_diffs.append(neighbor_rating - rating)
        new_edge.num_ratings = 1
        new_edge.mean_of_diffs = neighbor_rating-rating
        new_edge.stdev = 0
        new_edge.conf = 0
        new_edge.scaling_factor = (neighbor_item.nom_size*rating)/(float (item.nom_size*neighbor_rating))
        brand.edge_list.append (new_edge)
        opposite_edge = graph.Edge ()
        opposite_edge.neighbor_pointer = brand
        opposite_edge.list_of_diffs.append(rating - neighbor_rating) 
        opposite_edge.num_ratings = 1
        opposite_edge.mean_of_diffs = - new_edge.mean_of_diffs
        opposite_edge.stdev = 0
        opposite_edge.conf = 0
        opposite_edge.scaling_factor = 1/new_edge.scaling_factor
        neighbor_brand.edge_list.append (opposite_edge)
      else: # if   brands are already connected
        new_edge = brand.edge_list[brand.neighbors_list().index (neighbor_brand)]
        new_edge.list_of_diffs.append(neighbor_rating - rating)
        new_edge.num_ratings += 1
        (new_edge.mean_of_diffs, new_edge.stdev) = update_mean_stdev(new_edge.mean_of_diffs, new_edge.stdev, new_edge.num_ratings, rating)
        new_edge.conf = interval.conf(new_edge.list_of_diffs)
        new_edge.scaling_factor = update_scale(len(new_edge.list_of_diffs), new_edge.scaling_factor, neighbor_item.nom_size, neighbor_rating, item.nom_size, rating)
        brand.edge_list[brand.neighbors_list().index (neighbor_brand)] = new_edge
        opposite_edge = neighbor_brand.edge_list[neighbor_brand.neighbors_list().index (brand)]
        opposite_edge.list_of_diffs.append(rating - neighbor_rating)
        opposite_edge.num_ratings += 1
        opposite_edge.mean_of_diffs = - new_edge.mean_of_diffs
        opposite_edge.stdev = new_edge.stdev
        opposite_edge.conf = new_edge.conf
        opposite_edge.scaling_factor = 1/new_edge.scaling_factor
        neighbor_brand.edge_list[neighbor_brand.neighbors_list().index (brand)] = opposite_edge

def update_users_list(userid, item, rating):
  global users_list
  user = users_list[userid]
  purchases = [purch[0] for purch in user.itemrating_list]
  if (item in purchases):
    pass
  else:
    user.itemrating_list.append((item, rating))

def Rate_Event (userid, item, rating): # do very similar thing to update brandgraph
  global itemgraph
  global brandgraph
  if item.is_new:
    new_item (item)
    update_users_list (userid, item, rating)
    update_new_item (item, userid, rating)
    update_user_items_new (item, userid, rating)
    if item.brandname not in brandgraph.brand_list () : # if brand isn't in brandgraph yet
      new_brand (item, rating)
      update_brands (userid, item, rating)
    else:
      update_brands (userid, item, rating)  
  else:
    update_users_list (userid, item, rating)
    update_existing_item (item, userid, rating)
    update_user_items_existing (item, userid, rating)
    if item.brandname not in brandgraph.brand_list () : # if brand isn't in brandgraph yet
      new_brand (item, rating)
      update_brands (userid, item, rating)
    else:
      update_brands (userid, item, rating)  
      
def Ask_For_Prediction_Event (userid, start_item):
  global users_list
  global itemgraph
  global brandgraph
  return pathfinder.pathfinder(start_item, users_list[userid])  
