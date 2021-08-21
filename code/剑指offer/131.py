"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。

示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：
输入：s = "a"
输出：[["a"]]
 
提示：
1 <= s.length <= 16
s 仅由小写英文字母组成

"""

class Solution(object):

    dp = None
    res = None

    def partition(self, s):
        self.res = []
        self.dp = [[False] * len(s) for i in range(len(s))]
        self.dp_function(s)
        self.find(s, 0, [])
        return self.res

    def dp_function(self, s):
        for x in range(len(s) - 1, -1 , -1):
            for y in range(x, len(s)):
                if x == y:
                    self.dp[x][y] = True
                    continue
                if x + 1 == y:
                    self.dp[x][y] = s[x] == s[y]
                    continue
                self.dp[x][y] = self.dp[x + 1][y - 1] and s[x] == s[y]

    def find(self, s, first_index, find_list):
        if first_index >= len(s):
            self.res.append(find_list)
            return
        for i in range(first_index, len(s)):
            if self.dp[first_index][i]:
                tmp_list = find_list[:]
                tmp_list.append(s[first_index:i + 1])
                self.find(s, i + 1, tmp_list)

s = Solution()
print(s.partition('abbab'))