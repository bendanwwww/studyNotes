"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
"""

class Solution(object):
    def exchange(self, nums):
        if len(nums) == 0:
            return nums
        left_index = 0
        right_index = len(nums) - 1
        while left_index < right_index:
            if nums[left_index] % 2 == 1:
                left_index += 1
            else:
                tmp = nums[right_index]
                nums[right_index] = nums[left_index]
                nums[left_index] = tmp
                right_index -= 1
        return nums

s = Solution()
print(s.exchange([1, 2, 3, 4]))