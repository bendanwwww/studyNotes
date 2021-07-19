"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1)

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
"""

class CQueue(object):

    add_stack = []
    delete_stack = []

    def __init__(self):
        self.add_stack = []
        self.delete_stack = []

    def appendTail(self, value):
        self.add_stack.append(value)


    def deleteHead(self):
        if len(self.delete_stack) == 0:
            while len(self.add_stack) > 0:
                self.delete_stack.append(self.add_stack.pop())
        if len(self.delete_stack) == 0:
            return -1
        else:
            return self.delete_stack.pop()


s = CQueue()
print(s.deleteHead())
s.appendTail(5)
s.appendTail(2)
print(s.deleteHead())
print(s.deleteHead())
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]