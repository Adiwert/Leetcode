# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val        # The value stored in the node
#         self.left = left      # Reference to the left child node
#         self.right = right    # Reference to the right child node
class Solution(object):
    def flipEquiv(self, root1, root2):      # "flipEquiv" function is to compare two binary trees (root1 and root2)
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if not root1 or not root2:          # Check if either of the tree is empty
            return not root1 and not root2  # If both trees are empty, return True, otherwise False

        if root1.val != root2.val:          # Check if the roots has the same value from both trees
            return False                    # It the roots are same, return True, otherwise the trees cannot be equivalent and return False
        
        a = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)             # Recursively check if the left and right subtrees are equivalent without flipping
        return a or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)     # Recursively check if the left and right subtrees are equivalent with flipping
    # The function returns True if either of the two scenarios is True

'''
At each recursive call, the function processes smaller and smaller subtrees until it reaches the leaf nodes (None).
This is how it breaks down the larger problem into smaller ones (which is a hallmark of recursion).
When both trees are fully compared (either matching or flipped), the recursion terminates.
'''