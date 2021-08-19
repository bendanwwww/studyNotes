"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

示例 1：
    3
   / \
  1   4
   \ 
    2 
输入：root = [3,1,4,null,2], k = 1
输出：1

示例 2：
       5
      / \
     3   6
    / \
   2   4
  /   
 1
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

提示：
树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104

进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    res = None
    index = 1
    def kthSmallest(self, root, k):
        if root.left is not None:
            self.kthSmallest(root.left, k)
        if self.index == k:
            self.res = root.val
        self.index += 1          
        if root.right is not None:
            self.kthSmallest(root.right, k)
        return self.res

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
s = Solution()
print(s.kthSmallest(root, 3))