class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            print('index out of bound')
            return

        counter = 0
        temp = self.head
        while counter < index and temp is not None:
            temp = temp.next
            counter += 1
        if counter == index:
            return temp.data
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        self.head = new_node
        new_node.next = temp


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

        return


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            print('Invalid postition')
            return
        if index == 0:
            new_node =Node(val)
            new_node.next = self.head
            self.head = new_node
            return
        if index == 1:
            new_node = Node(val)
            new_node.next = self.head.next
            self.head.next = new_node
            return

        counter = 0
        temp = self.head
        prev = None
        while temp:
            if counter == index:
                new_node = Node(val)
                prev.next = new_node
                new_node.next = temp
                return
            prev = temp
            temp = temp.next
            counter += 1
        return -1
            


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            print('index out of bound')
            return

        if index == 0:
            if self.head.next:
                self.head = self.head.next
                return
            self.head = None


        counter = 1
        temp = self.head
        while temp is not None:
            if counter == index:
                temp.next = temp.next.next
                return
            temp = temp.next
            counter += 1
        return -1

            

    def printll(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
        return

        


linkedList = MyLinkedList() # Initialize empty LinkedList
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
linkedList.get(1)            # returns 2
linkedList.deleteAtIndex(1)  # now the linked list is 1->3
linkedList.get(1)            # returns 3