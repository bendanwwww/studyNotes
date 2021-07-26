"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：
0 <= 链表长度 <= 1000
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = None
        node = head
        l1_node = l1
        l2_node = l2
        while l1_node is not None or l2_node is not None:
            if l1_node is None and l2_node is not None:
                if head is None:
                    head = l2_node
                else:
                    node.next = l2_node
                break
            if l2_node is None and l1_node is not None:
                if head is None:
                    head = l1_node
                else:
                    node.next = l1_node
                break
            if l1_node.val > l2_node.val:
                if head == None:
                    head = l2_node
                    node = head
                    l2_node = l2_node.next
                    continue
                node.next = l2_node
                node = l2_node
                l2_node = l2_node.next
            else:
                if head == None:
                    head = l1_node
                    node = head
                    l1_node = l1_node.next
                    continue
                node.next = l1_node
                node = l1_node
                l1_node = l1_node.next
        return head

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
s = Solution()
print(s.mergeTwoLists(None, head2))
