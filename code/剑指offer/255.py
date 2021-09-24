"""
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
你可以假定该序列中的数都是不相同的。
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [5,2,6,1,3]
输出: false

示例 2：
输入: [5,2,1,3,6]
输出: true

进阶挑战：
您能否使用恒定的空间复杂度来完成此题？

"""

class Solution(object):
    def verifyPreorder(self, preorder):
        return self.dsf(0, len(preorder) - 1, preorder)

    def dsf(self, left_index, right_index, preorder):
        if left_index >= right_index:
            return True
        root_val = preorder[left_index]
        mid_index = right_index + 1
        for i in range(left_index + 1, right_index + 1):
            if preorder[i] > root_val:
                mid_index = i
                break
        for i in range(mid_index, right_index + 1):
            if preorder[i] < root_val:
                return False
        return self.dsf(left_index + 1, mid_index - 1, preorder) and self.dsf(mid_index, right_index, preorder)

s = Solution()
print(s.verifyPreorder([5, 2, 1, 3, 6]))