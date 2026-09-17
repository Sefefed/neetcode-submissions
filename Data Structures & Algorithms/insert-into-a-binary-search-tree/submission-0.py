# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_Node = TreeNode(val)
        if not root:
            return new_Node
        cur = root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = new_Node
                    break
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = new_Node
                    break
                cur = cur.right
        return root                    



        
        