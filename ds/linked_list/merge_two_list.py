class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None

	def append(self, val):
		new_node = Node(val)

		if self.head is None:
			self.head = new_node
			return

		temp = self.head
		while temp.next is not None:
			temp = temp.next
		temp.next = new_node
		return

	def printll(self):
		if not self.head:
			print('Nothing to print')

		temp = self.head
		while temp.next is not None:
			print(temp.data)
			temp = temp.next


def merge_list(head1, head2):
	temp = None

	if head1 is None:
		return head2

	if head2 is None:
		return head1

	if head1.data <= head2.data:
		temp = head1
		temp.next = merge_list(head1.next, head2)
	else:
		temp = head2
		temp.next = merge_list(head1, head2.next)
	return temp

list1 = LinkedList() 
list1.append(5) 
list1.append(10)
list1.append(15) 
 
list2 = LinkedList() 
list2.append(2) 
list2.append(3) 
list2.append(20)

list3 = LinkedList() 
list3.head = merge_list(list1.head, list2.head) 

list3.printll()