"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2

给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true

限制：
0 <= 节点个数 <= 10000
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        if B is None:
            return False
        node_a_stack = []
        node_a_stack.append(A)
        while len(node_a_stack) > 0:
            node_a = node_a_stack[0]
            del node_a_stack[0]
            if node_a.left is not None:
                node_a_stack.append(node_a.left)
            if node_a.right is not None:
                node_a_stack.append(node_a.right)
            if self.dsf_check(node_a, B):
                return True
        return False
        
    def dsf_check(self, node_a, node_b):
        if node_b is None:
            return True
        if node_a is None or node_a.val != node_b.val:
            return False
        return self.dsf_check(node_a.left, node_b.left) and self.dsf_check(node_a.right, node_b.right)

s = Solution()
root_a = TreeNode(3)
root_a.left = TreeNode(4)
root_a.right= TreeNode(5)
root_a.left.left = TreeNode(1)
root_a.left.right = TreeNode(2)
root_b = TreeNode(4)
root_b.left = TreeNode(1)
print(s.isSubStructure(root_a, root_b))