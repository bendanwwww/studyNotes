"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        return self.handle(root, float('-inf'), float('inf'))

    def handle(self, root, lower, upper):
        if root.val >= upper or root.val <= lower:
            return False
        if root.left is not None and not self.handle(root.left, lower, root.val):
            return False
        if root.right is not None and not self.handle(root.right, root.val, upper):
            return False
        return True

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(7)
s = Solution()
print(s.isValidBST(root))