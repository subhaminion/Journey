class Node():
	def __init__(self, data):
		self.data = data
		self.next = next


class LinkedList():
	def __init__(self):
		self.head = None

	def push(self, data):
		# pushes data in the fron
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def append(self, data):
		# appends at the last
		new_node = Node(data)
		
		if self.head is None:
			self.head = new_node
			return

		tmp = self.head
		while tmp.next:
			tmp = tmp.next
		tmp.next = new_node

	def get_length(self):
		tmp = self.head
		counter = 0
		while tmp:
			tmp = tmp.next
			counter += 1

		return counter

	def print_list(self):
		tmp = self.head
		while tmp:
			print(tmp.data)
			tmp = tmp.next



	def reverse(self):
		prev = None
		current = self.head
		while (current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next

		self.head = prev


list1 = LinkedList() 
list1.push(10) 
list1.push(20) 
list1.push(30) 
list1.push(40)
list1.push(50)
list1.print_list()

list1.reverse()
print('----')
list1.print_list()

