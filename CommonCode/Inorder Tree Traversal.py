class Node:
       def __init__(self,key):
              self.left = None
	      self.right = None
	      self.key = key

       def inorder(self,root):
              if root:
                     inorder(root.left)
                     print(root)
                     print(root.right)


n1 = Node(1)
n1.left = Node(2)
n1.right =Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)

n1.inorder(n1)
