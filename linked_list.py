class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print all the elements in the linked list(Traverse)
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next

    # To add at the Beginning.
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        #Update the new node to be the head.
        NewNode.next = self.headval
        self.headval = NewNode

    # To add at the End
    def AtEnd(self, newdata):
        # Initialise the node.
        NewNode = Node(newdata)
        # If this is the first node make the current node as the Head node.
        if(self.headval == None):
            self.headval = NewNode
            return
        # Initialise a pointer pointing to the Head.
        last = self.headval
        while(last.next):
            last = last.next
        last.next = NewNode

# Creation of Nodes:
list = SLinkedList()# First Node of the Singly linked list
list.headval = Node("Mon") # Initialise the first node as the head.
list1 = Node("Tue")
list2 = Node("Wed")

# Linking Nodes:
# Link the first node to the second node.
list.headval.next = list1
# Link the second node to the third node.
list1.next = list2

list.AtBeginning("Sun")
list.AtBeginning("Sat")
list.AtEnd("Thu")

#Traverse a linked list.
list.listprint()
