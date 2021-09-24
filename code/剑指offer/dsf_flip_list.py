# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    new_head = None

    def dsf_flip_list(self, head):
        self.dsf(head)
        return self.new_head
    
    def dsf(self, node):
        if node.next is None:
            self.new_head = node
            return node
        tmp_node = node
        res_node = self.dsf(node.next)
        tmp_node.next = None
        res_node.next = tmp_node
        return tmp_node

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
new_head = s.isPalindrome(head)
print(new_head)