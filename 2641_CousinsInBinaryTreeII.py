from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
This would be a standard class definition for a binary tree node, 
where each node has a value (val), a left child (left), and a right child (right).
'''
class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        '''
        This defines a class Solution with a method replaceValueInTree.
        This method will take the root of a binary tree (root) as input and return the modified tree.
        The method uses Breadth-First Search (BFS) to traverse the tree level by level.
        '''
        level_sum=[] # This will store the sum of all node values for each level

        q = deque([root])                   # deque (double-ended queue) q is initialized with the root node as the first element
        while q:                            # As long as there are nodes in the queue q
            cur_sum = 0                     # Initialize cur_sum to 0 for the current level and to hold the sum of node values for the current level

            for i in range(len(q)):         # The loop iterates over all nodes in the current level
                node = q.popleft()          # popleft() removes and returns the leftmost node (initial/parent node) from the queue
                cur_sum += node.val         # The dequeued node value is added to cur_sum
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)    # If the current node has a left or right child, append the child (node) to the queue
            level_sum.append(cur_sum)       # After processing all nodes in the current level, append cur_sum to level_sum, then move to the next level

        q = deque([(root, root.val)])   # (node, child_sum)
        level = 0                       # Start from the root level
        while q:                                        # As long as there are nodes in the queue q
            for i in range(len(q)):                     # The loop iterates over all nodes in the current level
                node, val = q.popleft()                 # Leftmost node and its value (initial/parent node and its value) are remove from the queue
                node.val = level_sum[level] - val       # The node's value is updated with the sum for the current level minus the node's original value
                child_sum = 0                           # child_sum is initialised to 0 and to hold the sum of the values of the current node's children
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val         # If the current node has a left or right child, add the child (node) value to child_sum
                if node.left:
                    q.append((node.left, child_sum))
                if node.right:
                    q.append((node.right, child_sum))   # If the current node has a left or right child, append the child (node) to the queue along with its child_sum
            level += 1                                  # Move to the next level in the tree

        return root     # Modified root of the binary tree is returned