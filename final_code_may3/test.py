import random
import helpers
import graph
from collections import defaultdict
from helpers import users_list, items_list, itemgraph, brandgraph
import recommendations
import findcoeffs

max_users = 6
num_items = 30
def dump (G, parameter):
  adjmat = defaultdict(dict)
  print("Name: " + G.name)
  num_v = len(G.item_list)
  for i in G.item_list:
    for j in G.item_list:
      adjmat[i][j] = 0

  for i in G.item_list:
    for j in i.edge_list:
      if (parameter == "conf"):
        adjmat[i][j.neighbor_pointer] = j.conf
      elif (parameter == "num"):
        adjmat[i][j.neighbor_pointer] = j.num_ratings
      elif (parameter == "scale"):
        adjmat[i][j.neighbor_pointer] = "|"+str(j.scaling_factor)+";"+str(j.num_ratings)+"|"       
      else:
        adjmat[i][j.neighbor_pointer] =  "|"+str("{0:.2f}".format(j.conf))+ ";"+str("{0:.2f}".format(j.stdev))+ ";"+ str(j.num_ratings)+"|"

  for i in G.item_list:
    for j in G.item_list:
      print(adjmat[i][j]), 
    print

def init_rand_users():
  global users_list
  for i in range(0,max_users):
    size = random.randint(20,80)
    user = graph.User()
    user.size = size
    helpers.create_user(user)
  return users_list

def get_items():
  global items_list
  for i in range(0,num_items):
    id = i
    name = "product_"+str(i)
    brand_id = random.randint(0,10)
    brandname = "brand_"+str(brand_id)
    nom_size = random.randint(1,100)
    act_size = None
    num_ratings = 0
    avg_rating = 0
    edge_list = []
    is_new = True
    item = graph.Item(id, name, brandname, nom_size, act_size, num_ratings, avg_rating, edge_list, is_new)
    items_list.append(item)
  return items_list

def make_purchases(max_events):
  for i in range(0, max_events):
    userid = random.randint(0,max_users-1)
    user = users_list[userid]
    itemid = random.randint(0,num_items-1)
    item = items_list[itemid]
    purchases = [purch[0] for purch in user.itemrating_list]
    if (item in purchases):
      pass
    else:
      while abs(item.nom_size - user.size) > 20:
        itemid = random.randint(0,num_items-1)
        item = items_list[itemid]
      rating = (item.nom_size - user.size + 50) + random.randrange(-5,5)
      helpers.Rate_Event(userid, item, rating)
    
init_rand_users()
get_items()
make_purchases(120)
# choose 2nd parameter from conf, num, or basic
dump(itemgraph, "num")
dump(brandgraph, "num")

print(findcoeffs.find_coeffs())

for i in range(0, len(itemgraph.item_list)):
  if (itemgraph.item_list[i] not in [x[0] for x in users_list[0].itemrating_list]):
    print helpers.Ask_For_Prediction_Event (users_list[0].id, itemgraph.item_list[i])
    break
for i in range(0, max_users):
  print "User "+str(i)
  rec = recommendations.recommendations(users_list[i], 3)
  if (rec != []):
    for rec_item in rec:
      print rec_item[0].name
      print rec_item[1]
      print rec_item[2]
  else:
    print "No edges emanating from this user's items."
  print