
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,small,large):
            if not node:
                return True 
            if not (small < node.val < large):
                return False 
            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
        