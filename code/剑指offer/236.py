"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1

提示：
树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    p_road = []
    q_road = []
    def lowestCommonAncestor(self, root, p, q):
        self.p_road = []
        self.q_road = []
        self.find_road(root, p.val, q.val, [])
        res = None
        for i in range(max(len(self.p_road), len(self.q_road))):
            if i >= len(self.p_road) or i >= len(self.q_road):
                break
            if self.p_road[i].val == self.q_road[i].val:
                res = self.p_road[i]
        return res

    def find_road(self, node, p, q, road):
        if node == None:
            return
        road.append(node)
        if node.val == p:
            self.p_road = road[:]
        if node.val == q:
            self.q_road = road[:]
        if node.left is not None:
            self.find_road(node.left, p, q, road[:])
        if node.right is not None:
            self.find_road(node.right, p, q, road[:])
        
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
s = Solution()
print(s.lowestCommonAncestor(root, 5, 1))