class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverseAndPrint(head):
    Currentnode=head
    while Currentnode:
        print(Currentnode.data, end=" , ")
        Currentnode=Currentnode.next
    print("null")


node1 = Node(5)
node2 = Node(6)
node3 = Node(19)
node4 = Node(25)
node5 = Node(46)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
traverseAndPrint(node1)