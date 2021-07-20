"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000
"""

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        row_index = 0
        column_index = 0
        while row_index < len(matrix):
            if len(matrix[row_index]) == 0:
                return False
            if matrix[row_index][column_index] == target:
                return True
            is_add = True
            if matrix[row_index][column_index] > target:
                is_add = False
            while column_index >= 0 and column_index < len(matrix[0]):
                # print(matrix[row_index][column_index])
                if matrix[row_index][column_index] == target:
                    return True
                else:
                    if is_add:
                        if matrix[row_index][column_index] > target or column_index == len(matrix[0]) - 1:
                            break
                        column_index += 1
                    else:
                        if matrix[row_index][column_index] < target or column_index == 0:
                            break
                        column_index -= 1
            row_index += 1
        return False

matrix = [[1]
        ]
s = Solution()
print(s.findNumberIn2DArray(matrix, 13))