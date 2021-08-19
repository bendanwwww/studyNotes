"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        res = []
        if root is None:
            return res
        last_level = []
        last_level.append(root)
        while len(last_level) > 0:
            res_level = []
            node_level = []
            for n in last_level:
                res_level.append(n.val)
                if n.left is not None:
                    node_level.append(n.left)
                if n.right is not None:
                    node_level.append(n.right)
            res.append(res_level)
            last_level = node_level
        return res

root = TreeNode(2)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.levelOrder(root))