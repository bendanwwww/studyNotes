"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

"""

class Solution(object):
    def longestPalindrome(self, s):
        max_str = ''
        dp = [[False] * len(s) for i in range(len(s))]
        for x in range(len(s) - 1, -1, -1):
            for y in range(x, len(s)):
                if x == y:
                    dp[x][y] = True
                elif x + 1 == y:
                    dp[x][y] = s[x] == s[y]
                else:
                    dp[x][y] = dp[x + 1][y - 1] and s[x] == s[y]
                if dp[x][y] and y - x + 1 > len(max_str):
                    max_str = s[x: y + 1]
        return max_str

s = Solution()
print(s.longestPalindrome('babad'))
        