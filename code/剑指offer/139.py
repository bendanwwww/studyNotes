"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        word_stack = []
        left_index = 0
        right_index = 0
        while True:
            is_in_word_dict = False
            for right in range(right_index, len(s)):
                tmp_str = s[left_index: right + 1]
                if tmp_str in wordDict:
                    word_stack.append([left_index, right])
                    is_in_word_dict = True
                    right_index = right + 1
                    left_index = right_index
                    break
            if is_in_word_dict and right_index == len(s):
                return True
            if is_in_word_dict:
                continue
            if len(word_stack) == 0:
                break
            last_index = word_stack.pop()
            left_index = last_index[0]
            right_index = last_index[1] + 1
        return False

s = Solution()
print(s.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))

"""
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
"""