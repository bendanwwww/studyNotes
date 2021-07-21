"""
地上有一个m行n列的方格，从坐标 [0, 0] 到坐标 [m-1, n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20
"""

class Solution(object):
    def movingCount(self, m, n, k):
        find_load = []
        load = []
        load_stack = []
        load_stack.append([0, 0])
        find_load.append([0, 0])
        while len(load_stack) > 0:
            in_load = load_stack.pop()
            load_num_str = str(in_load[0]) + str(in_load[1])
            load_num = 0
            for s in load_num_str:
                load_num += int(s)
            if load_num <= k:
                load.append(in_load)
                # 上下左右放入栈
                if in_load[0] - 1 >= 0 and [in_load[0] - 1, in_load[1]] not in find_load:
                    load_stack.append([in_load[0] - 1, in_load[1]])
                    find_load.append([in_load[0] - 1, in_load[1]])
                if in_load[0] + 1 < m and [in_load[0] + 1, in_load[1]] not in find_load:
                    load_stack.append([in_load[0] + 1, in_load[1]])
                    find_load.append([in_load[0] + 1, in_load[1]])
                if in_load[1] - 1 >= 0 and [in_load[0], in_load[1] - 1] not in find_load:
                    load_stack.append([in_load[0], in_load[1] - 1])
                    find_load.append([in_load[0], in_load[1] - 1])
                if in_load[1] + 1 < n and [in_load[0], in_load[1] + 1] not in find_load:
                    load_stack.append([in_load[0], in_load[1] + 1])
                    find_load.append([in_load[0], in_load[1] + 1])
        return len(load)

s = Solution()
print(s.movingCount(16, 8, 4))