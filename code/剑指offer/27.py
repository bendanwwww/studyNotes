"""
给定一个链表的 头节点 head ，请判断其是否为回文链表。
如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。

示例 1：
输入: head = [1,2,3,3,2,1]
输出: true

示例 2：
输入: head = [1,2]
输出: false

提示：
链表 L 的长度范围为 [1, 10^5]
0 <= node.val <= 9
 
进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution(object):

#     new_head = None

#     def isPalindrome(self, head):
        
    
#     def dsf(self, node):
        
        
# s = Solution()
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# new_head = s.isPalindrome(head)
# print(new_head)