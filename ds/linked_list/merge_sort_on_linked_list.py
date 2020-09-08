class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LL:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return
		temp = self.head
		while temp.next is not None:
			temp = temp.next
		temp.next = new_node

	# utility function to get middle of linked list
	def get_middle(self, head):
		if head == None:
			return head

		slow = head
		fast = head

		while (fast.next != None and fast.next.next != None):
			slow = slow.next
			fast = fast.next.next

		return slow

	def sorted_merge(self, a, b):
		result = None

		# base cases
		if a == None:
			return b
		if b == None:
			return a

		if a.data <= b.data:
			result = a
			result.next = self.sorted_merge(a.next, b)
		else:
			result = b
			result.next = self.sorted_merge(a, b.next)
		return result

	def merge_sort(self, head):
		
		# base case
		if head == None or head.next == None:
			return head

		# getting the middle of the list
		middle = self.get_middle(head)
		next_to_middle = middle.next

		middle.next = None

		left = self.merge_sort(head)
		right = self.merge_sort(next_to_middle)

		sortedlist = self.sorted_merge(left, right)
		return sortedlist


def printList(head): 
    if head is None: 
        print(' ') 
        return
    curr_node = head 
    while curr_node: 
        print(curr_node.data, end = " ") 
        curr_node = curr_node.next
    print(' ')


li = LL() 
  
# Let us create a unsorted linked list 
# to test the functions created.  
# The list shall be a: 2->3->20->5->10->15  
li.append(5) 
li.append(20)
li.append(10) 
li.append(2) 
li.append(15) 
li.append(3)
  
# Apply merge Sort  
print('before sort')
printList(li.head) 
li.head = li.merge_sort(li.head) 

print ("Sorted Linked List is:") 
printList(li.head) 
