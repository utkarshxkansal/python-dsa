"""LeetCode 104 — Maximum Depth of Binary Tree.

Time: O(n) | Space: O(h) recursion stack
"""


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)
