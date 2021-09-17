"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

提示：
数组长度 <= 1000

"""

class Solution(object):
    def verifyPostorder(self, postorder):
        return self.dsf(0, len(postorder) - 1, postorder)
        
    def dsf(self, left_index, right_index, postorder):
        if left_index >= right_index:
            return True
        root_val = postorder[right_index]
        mid_index = right_index
        for i in range(left_index, right_index):
            if postorder[i] > root_val:
                mid_index = i
                break
        for i in range(mid_index, right_index):
            if postorder[i] < root_val:
                return False
        return self.dsf(left_index, mid_index - 1, postorder) and self.dsf(mid_index, right_index - 1, postorder)

s = Solution()
print(s.verifyPostorder([4, 6, 7, 5]))