class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self,root):
        if not root:
            return

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    

## creating a Tree-----
t = TreeNode(4)
t1 = TreeNode(2)
t2 = TreeNode(7)
t3 = TreeNode(1)
t4 = TreeNode(3)
t5 = TreeNode(6)
t6 = TreeNode(9)

t.left = t1
t.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
## --------------------

print("Traversing Inorder for Actual Tree")
inorder(t)
print("Traversing Inorder for Inverted Tree")
inorder(Solution().invertTree(t))
