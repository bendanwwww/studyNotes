"""
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。

示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912

进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?
示例：
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_index = l1
        l2_index = l2
        add_byte = 0
        res_head = None
        res_last = None
        while l1_index is not None and l2_index is not None:
            tmp_add = l1_index.val + l2_index.val
            if add_byte == 1:
                tmp_add += 1
            if tmp_add >= 10:
                tmp_add = tmp_add % 10
                add_byte = 1
            else:
                add_byte = 0
            l1_index = l1_index.next
            l2_index = l2_index.next
            node = ListNode(tmp_add)
            if res_head is None:
                res_head = node
            else:
                res_last.next = node
            res_last = node

        while l1_index is not None:
            if add_byte == 1:
                l1_index.val += 1
            if l1_index.val >= 10:
                l1_index.val = l1_index.val % 10
                add_byte = 1
            else:
                add_byte = 0
            node = ListNode(l1_index.val)
            res_last.next = node
            res_last = node
            l1_index = l1_index.next
        while l2_index is not None:
            if add_byte == 1:
                l2_index.val += 1
            if l2_index.val >= 10:
                l2_index.val = l2_index.val % 10
                add_byte = 1
            else:
                add_byte = 0
            node = ListNode(l2_index.val)
            res_last.next = node
            res_last = node
            l2_index = l2_index.next
        if add_byte == 1:
            res_last.next = ListNode(1)
        return res_head

    def addTwoNumbers2(self, l1, l2):
        node_res = self.dsf(l1, l2)
        if node_res[1] == 1:
            node = ListNode(1)
            node.next = node_res[0]
            node_res[0] = node
        return node_res[0]

    def dsf(self, node1, node2):
        if node1 is None:
            return [None, 0]
        val1 = node1.val
        val2 = node2.val
        next_node_res = self.dsf(node1.next, node2.next)
        tmp_add = val1 + val2 + next_node_res[1]
        node = ListNode(tmp_add % 10)
        node.next = next_node_res[0]
        return [node, tmp_add >= 10]

s = Solution()
l1_head = ListNode(1)
l1_head.next = ListNode(1)
l1_head.next.next = ListNode(6)
l2_head = ListNode(9)
l2_head.next = ListNode(9)
l2_head.next.next = ListNode(2)
new_head = s.addTwoNumbers2(l1_head, l2_head)
print(new_head)