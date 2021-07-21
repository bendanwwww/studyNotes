"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

限制：
0 <= 链表长度 <= 10000
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, c):
        head = c
        if head is None:
            return []
        node = head
        next_node = node.next
        node.next = None
        while next_node is not None:
            tmp_next_node = next_node.next
            next_node.next = node
            node = next_node
            next_node = tmp_next_node
        res = []
        while node is not None:
            res.append(node.val)
            node = node.next
        return res

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
s = Solution()
print(s.reversePrint(head))