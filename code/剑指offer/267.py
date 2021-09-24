"""
给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。
如不能形成任何回文排列时，则返回一个空列表。

示例 1：
输入: "aabb"
输出: ["abba", "baab"]

示例 2：
输入: "abc"
输出: []

"""

class Solution(object):
    def generatePalindromes(self, s):
        word_num_dict = {}
        for w in s:
            if w in word_num_dict:
                word_num_dict[w] += 1
            else:
                word_num_dict[w] = 1
        