#Helpers.py
 
#Global Variables
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

def get_item_from_id (itemgraph, id):
  itemgraph.itemlist[itemgraph.itemid_list.index (id)]

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

def new_item (graph, item, rating):	
	global current_item_id
	item.id = current_item_id
	current_item_id += 1
	item.is_new = False
	graph.item_list.append (item)

def update_new_item (item, userid, rating):
	global users_list
	if users_list[userid].itemrating_list == []:
		pass
	else:	
		for (neighbor_item, neighbor_rating) in users_list[userid]:
			edge = Edge ()
			edge.neighbor_item = neighbor_item
			edge.list_of_diffs.append (rating - neighbor_rating)
			edge.num_ratings += 1
			edge.mean_diffs =  sum (list_of_diffs) / edge.num_ratings
			edge.stdev = 0
			edge.conf = conf(list_of_diffs)
			item.edge_list.append (edge)

def update_user_items_new (itemgraph, item, userid, rating):
    global users_list
    if users_list[userid].itemrating_list == []:
            pass
    else:	
            for (neighbor_item, neighbor_rating) in users_list[userid]:
                    if neighbor_item == item:
                            pass
                    else:	                           
                            edge = Edge ()
                            edge.neighbor_item = item
                            edge.list_of_diffs.append (neighbor_rating - rating)
                            edge.num_ratings += 1
                            edge.mean_diffs =  sum (list_of_diffs) / edge.num_ratings
                            edge.stdev = 0
                            edge.conf = conf(list_of_diffs)
                            user_item.edge_list.append (edge)	

def update_existing_item (item, userid, rating):
	global users_list
	if users_list[userid].itemrating_list == []:
		pass
	else:	
		for (neighbor_item, neighbor_rating) in users_list[userid]:
			if neighbor_item in item.neighbors_list():
				edge = item.edge_list[item.edge_list.index (neighbor_item.id)]
				edge.list_of_diffs.append (rating - neighbor_rating)
				edge.num_ratings += 1
				(edge.mean_diffs, edge.stdev) = sitan_update(edge.mean_diffs, edge.stdev, edge.num_ratings, (rating - neighbor_rating))
				edge.conf = conf(list_of_diffs)
				item.edge_list[item.edge_list.index (neighbor_item.id)] = edge
			else:
				edge = Edge () 
				edge.neighbor_item = neighbor_item
				edge.list_of_diffs.append (rating - neighbor_rating)
				edge.num_ratings += 1
				edge.mean_diffs =  sum (list_of_diffs) / edge.num_ratings
				edge.stdev = 0
				edge.conf = conf(list_of_diffs)
				user_item.edge_list.append (edge)

def update_user_items_existing (itemgraph, item, userid, rating):
	global users_list
	if users_list[userid].itemrating_list == []:
		pass
	else:
		for (neighbor_item, neighbor_rating) in users_list[userid]:
			if neighbor_item == item:
				pass
			else:	
				if item.id in neighbor_item.neighbors_list():
					edge = neighbor_item.edge_list[neighbor_item.edge_list.index (item.id)]
					edge.list_of_diffs.append (neighbor_rating - rating)
					edge.num_ratings += 1
					(edge.mean_diffs, edge.stdev) = sitan_update(edge.mean_diffs, edge.stdev, edge.num_ratings, (rating - neighbor_rating))
					edge.conf = conf(list_of_diffs)
					user_item.edge_list[user_item.edge_list.index (item.id)] = edge
				else:
					edge = Edge ()
					edge.neighbor_item = item
					edge.list_of_diffs.append (neighbor_rating - rating)
					edge.num_ratings += 1
					edge.mean_diffs =  sum (list_of_diffs) / edge.num_ratings
					edge.stdev = 0
					edge.conf = conf(list_of_diffs)
					user_item.edge_list.append (edge)	

def Rate_Event (itemgraph, brandgraph, userid, item, rating): # do very similar thing to update brandgraph
	if item.is_new:
		new_item (itemgraph, item, rating)
		update_new_item (item, userid, rating)
		update_user_items_new (itemgraph, item, userid, rating)
	else:
		update_existing_item (item, userid, rating)
		update_user_items_existing (itemgraph, item, userid, rating)

def Ask_For_Prediction_Event (itemgraph, brandgraph, userid, start_item):
	global users_list
	pathfinder(itemgraph, start_item, users_list[userid])	
