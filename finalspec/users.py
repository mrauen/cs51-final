# users.py
# Contains type definitions and values for user.

class User:
	def __init__ (self, user_id = 0, username = "", itemidlist = {}):
		self.user_id = user_id
		self.username = username
		self.itemidlist = itemidlist