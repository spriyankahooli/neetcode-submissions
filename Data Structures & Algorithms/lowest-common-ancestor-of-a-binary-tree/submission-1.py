# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        parent = {root: None}
        queue = deque([root])
        ancestor = set()
        while queue:

            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        current  = p
        while current:
            ancestor.add(current)
            current = parent[current]
        current = q
        while current not in ancestor:
            current = parent[current]
        return current