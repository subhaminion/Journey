import random

class Node(object):
	def __init__(self, key, level):
		self.key = key
		self.forward = [None] * (level+1)

class Skiplist(object):
	def __init__(self, max_level, p):
		self.max_level = max_level

		self.p = p
		self.header = self.create_node(self.max_level, -1)
		