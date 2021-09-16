"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：
输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
 
提示：
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 按 严格递增 顺序排列

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.dsf(nums, 0, len(nums) - 1)
    
    def dsf(self, nums, left_index, right_index):
        if left_index > right_index:
            return None
        mid_index = int((left_index + right_index) / 2)
        node = TreeNode(nums[mid_index])
        node.left = self.dsf(nums, left_index, mid_index - 1)
        node.right = self.dsf(nums, mid_index + 1, right_index)
        return node

s = Solution()
head = s.sortedArrayToBST([-10, -3, 0, 5, 9])
print(head)