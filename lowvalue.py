class Node:
    x = []

    def __init__(self, data):
        self.data = data
        self.next = None


def trans(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" , ")
        currentNode = currentNode.next


def lowvalue(head):
    low = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < low:
            low = currentNode.data
        currentNode = currentNode.next
    return low


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
trans(node1)
print("\n lowest value",lowvalue(node1))