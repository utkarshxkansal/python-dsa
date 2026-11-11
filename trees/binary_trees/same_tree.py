"""LeetCode 100 — Same Tree.

Two trees are the same when their structure and corresponding node values match.

Time: O(n) | Space: O(h) recursion stack
"""


class Solution:
    def isSameTree(self, p, q):
        # Both nodes are empty.
        if p is None and q is None:
            return True

        # Only one node is empty: structures differ.
        if p is None or q is None:
            return False

        # Corresponding values must match.
        if p.val != q.val:
            return False

        # Both left and right subtrees must be identical.
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
