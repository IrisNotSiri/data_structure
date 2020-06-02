class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    # assume data is a string
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

ll.remove("first")
print(ll)


from collections import deque
llis = deque('abdedc')
llis.appendleft('t')
llis.popleft()
print (llis)


# create tree node (both tree and binary search tree need tree node)
class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def __repr__(self):
      return str(self.data)

#create tree 
class Tree:
  def __init__(self):
    self.root = None
  # insert value in level order(to empty spot), in order of from high level to low level, from left to right
  def insert(self,temp,newNode):
    q = []
    q.append(temp)
    while (len(q)):
      temp = q[0]
      q.pop(0)
      if (not temp.left):
        temp.left = newNode
        break
      else:
        q.append(temp.left)
      if (not temp.right):
        temp.right = newNode
        break
      else:
        q.append(temp.right)


## create binary search tree

class BinarySearchTree:
    def __init__(self):
      self.root = None
    def insert(self,root,newNode):
      self.root = root
      if self.root.data < newNode.data:
        if self.root.right is None:
          self.root.right = newNode
        else:
          self.insert(self.root.right,newNode)
      else:
        if self.root.left is None:
          self.root.left = newNode
        else:
          self.insert(self.root.left, newNode)


"""
Tree Traversals (Inorder, Preorder and Postorder)
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right) 
(c) Postorder (Left, Right, Root) 
"""
def inorder(root): 
    if root: 
      #recur on left child
      inorder(root.left)
      #print the data of the node
      print (root.data)
      #recur on the right child
      inorder(root.right)
        
def postorder(root):
    if root:
      postorder(root.left)
      postorder(root.right)
      print(root.data)

def preorder(root):
    if root:
      print(root.data)
      preorder(root.left)
      preorder(root.right)
  
# Driver program to test the above functions 
# Let us create the following BST 
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 

#create binary search tree
r = TreeNode(50)
tree = BinarySearchTree()

tree.insert(r,TreeNode(30)) 
tree.insert(r,TreeNode(20)) 
tree.insert(r,TreeNode(40)) 
tree.insert(r,TreeNode(70)) 
tree.insert(r,TreeNode(60)) 
tree.insert(r,TreeNode(80)) 
  
# Print inoder traversal of the BST 
preorder(r)




        


      
      


      

