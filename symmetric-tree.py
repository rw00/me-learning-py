class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution.areEqual(root.left, root.right)

    def areEqual(left, right):
        if not left:
            return not right
        if not right:
            return False
        return left.val == right.val and Solution.areEqual(left.right, right.left) and Solution.areEqual(left.left, right.right)
