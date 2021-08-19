"""
给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。 

示例 1:
    3
   / \
  9  20
    /  \
   15   7
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

示例 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

提示:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均无重复元素
inorder 均出现在 preorder
preorder 保证为二叉树的前序遍历序列
inorder 保证为二叉树的中序遍历序列

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    pre_index = 0

    def buildTree(self, preorder, inorder):
        return self.handle(preorder, inorder, 0, len(inorder) - 1)

    def handle(self, preorder, inorder, in_left_index, in_right_index):
        if self.pre_index >= len(preorder):
            return None
        node = TreeNode(preorder[self.pre_index])
        in_index = in_left_index
        for i in range(in_left_index, in_right_index + 1):
            if inorder[i] == preorder[self.pre_index]:
                in_index = i
                break
        self.pre_index += 1
        if in_index - 1 >= in_left_index:
            node.left = self.handle(preorder, inorder, in_left_index, in_index - 1)
        if in_index + 1 <= in_right_index:
            node.right = self.handle(preorder, inorder, in_index + 1, in_right_index)
        return node

s = Solution()
head = s.buildTree([3, 1, 2, 4], [1, 2, 3, 4])
print(head)