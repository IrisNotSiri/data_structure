class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
          nodes.append(node.data)
          node = node.next
      nodes.append("None")
      return " -> ".join(nodes)
    def add(self, newNode):
      if self.head == None:
        self.head = newNode
      else:
        newNode.next = self.head
        self.head = newNode
    def remove(self, target):
      if(self.head != None and self.head.data == target):
        self.head = self.head.next
      prev = None
      curr = self.head
      while curr != None:
        if(curr.data == target):
          prev.next = curr.next
        prev = curr
        curr = curr.next



ll=LinkedList()

nodeThird = Node("third")
ll.add(nodeThird)
nodeSecond = Node("second")
ll.add(nodeSecond)
nodeFirst = Node("first")
ll.add(nodeFirst)

print(ll)

ll.remove("second")
print(ll)


# from collections import deque
# llis = deque('abdedc')
# llis.appendleft('t')
# llis.popleft()
# print (llis)


        
      

