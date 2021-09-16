"""
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

示例 1：
输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。

示例 2：
输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

提示：
1 <= s.length <= 10^4
s 仅由小写英文字母组成
1 <= k <= 10^5

"""

import re

class Solution(object):
    def longestSubstring(self, s, k):
        return self.dsf(s, k, 0, len(s) - 1)

    def dsf(self, s, k, left_index, right_index):
        word_num_map = {}
        for i in range(left_index, right_index + 1):
            if s[i] not in word_num_map:
                word_num_map[s[i]] = 1
            else:
                word_num_map[s[i]] += 1
        split_list = []
        for w in word_num_map:
            if word_num_map[w] < k:
                split_list.append(w)
        if len(split_list) == 0:
            return right_index - left_index + 1
        l = left_index
        r = l
        res = 0
        while r <= right_index:
            if s[r] not in split_list:
                r += 1
            else:
                res = max(res, self.dsf(s, k, l, r - 1))
                l = r + 1
                r = l
        return max(res, self.dsf(s, k, l, r - 1))

s = Solution()
print(s.longestSubstring('bbaaacbd', 3))