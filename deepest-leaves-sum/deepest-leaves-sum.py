# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = []
        sol = 0
        queue.append([root])
        
        while queue:
            nodes = queue.pop(0)
            
            if len(nodes)==0:
                break
            
            sol = 0
            next_depth = []
            
            for node in nodes:
                left = node.left
                right = node.right

                if left==None and right==None:
                    sol += node.val
                if left:
                    next_depth.append(left)
                if right:
                    next_depth.append(right)
            
            queue.append(next_depth)
            
        return sol
