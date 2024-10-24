# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val        # The value stored in the node
#         self.left = left      # Reference to the left child node
#         self.right = right    # Reference to the right child node
class Solution(object):
    def flipEquiv(self, root1, root2):      # 
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False
        
        a = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        return a or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)