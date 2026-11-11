"""LeetCode 102 — Binary Tree Level Order Traversal.

Visit nodes level by level from left to right using a queue.

Time: O(n) | Space: O(n)
"""

from collections import deque


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result
