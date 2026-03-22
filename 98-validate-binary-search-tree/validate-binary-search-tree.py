# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack = [(root, None, None)]
        
        while stack:
            node, low, high = stack.pop()
            
            if node is None:
                continue
            
            if low is not None and node.val <= low:
                return False
            
            if high is not None and node.val >= high:
                return False
            
            if node.right is not None:
                stack.append((node.right, node.val, high))
            
            if node.left is not None:
                stack.append((node.left, low, node.val))
            
        return True
        