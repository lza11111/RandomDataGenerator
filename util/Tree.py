class TreeNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.left = self.right = next

    @staticmethod
    def insertBSTNode(root, node):
        if root is None:
            return node
        curt = root
        while curt != node:
            if node.val < curt.val:
                if curt.left is None:
                    curt.left = node
                curt = curt.left
            else:
                if curt.right is None:
                    curt.right = node
                curt = curt.right
        return root