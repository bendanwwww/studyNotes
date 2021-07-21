"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

    A B C E
    S F C S
    A D E E

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 
提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成

"""

class Solution(object):
    def exist(self, board, word):
        for r in range(len(board)):
            for c in range(len(board[r])):
                if self.find(board, word, 0, [r, c], []):
                    return True
        return False

    def find(self, board, word, index, board_index, load):
        if index == len(word):
            return True
        if board_index in load:
            return False
        if board_index[0] < 0 or board_index[0] >= len(board) or board_index[1] < 0 or board_index[1] >= len(board[0]):
            return False
        if board[board_index[0]][board_index[1]] != word[index]:
            return False
        # 遍历上下左右
        load_copy = load[:]
        load_copy.append(board_index)
        if self.find(board, word, index + 1, [board_index[0] - 1, board_index[1]], load_copy):
            return True
        if self.find(board, word, index + 1, [board_index[0] + 1, board_index[1]], load_copy):
            return True
        if self.find(board, word, index + 1, [board_index[0], board_index[1] - 1], load_copy):
            return True
        if self.find(board, word, index + 1, [board_index[0], board_index[1] + 1], load_copy):
            return True
        return False
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
s = Solution()
print(s.exist(board, 'ABCCED'))