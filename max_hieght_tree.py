class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def height_tree(A):
    if(A==None):
        return 0
    else:
        ldepth=height_tree(A.left)
        rdepth=height_tree(A.right)
        if(ldepth>rdepth):
            return(1+ldepth)
        else:
            return(1+rdepth)
        
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.right=Node(7)
root.right.right=Node(6)

print(height_tree(root))