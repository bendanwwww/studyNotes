"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        quick_index = 0
        quick_node = head
        last_slow_node = None
        slow_node = head
        while quick_index < n:
            quick_node = quick_node.next
            quick_index += 1
        while quick_node is not None:
            last_slow_node = slow_node
            slow_node = slow_node.next
            quick_node = quick_node.next
        if last_slow_node is None:
            head = slow_node.next
        else:
            last_slow_node.next = slow_node.next
        return head

head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
s = Solution()
head = s.removeNthFromEnd(head, 1)
print(head)