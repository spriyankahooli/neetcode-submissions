# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None 
        parent = {root:None}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        ancestor = set()
        current = p
        while current:
            ancestor.add(current)
            current = parent[current]
        current = q 
        while current not in ancestor:
            current = parent[current]
        return current
