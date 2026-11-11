"""Preorder, inorder and postorder traversals using one stack.

Preorder:  Root -> Left -> Right
Inorder:   Left -> Root -> Right
Postorder: Left -> Right -> Root

Time: O(n) | Space: O(n)
"""


class Solution:
    def allTraversals(self, root):
        preorder = []
        inorder = []
        postorder = []

        if root is None:
            return [preorder, inorder, postorder]

        # Each pair stores (node, state).
        # 1 = preorder visit, 2 = inorder visit, 3 = postorder visit.
        stack = [(root, 1)]

        while stack:
            node, state = stack.pop()

            if state == 1:
                preorder.append(node.val)
                stack.append((node, 2))

                if node.left is not None:
                    stack.append((node.left, 1))

            elif state == 2:
                inorder.append(node.val)
                stack.append((node, 3))

                if node.right is not None:
                    stack.append((node.right, 1))

            else:
                postorder.append(node.val)

        return [preorder, inorder, postorder]
