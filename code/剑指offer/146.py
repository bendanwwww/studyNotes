"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 
进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 
提示：
1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put

"""

class LRUNode(object):
    def __init__(self, key, val, last=None, next=None):
        self.key = key
        self.val = val
        self.last = last
        self.next = next

class LRUCache(object):

    cache_map = {}
    lru_head = None
    lru_tail = None
    lru_size = 0
    capacity = 0

    def __init__(self, capacity):
        self.cache_map = {}
        self.lru_head = None
        self.lru_tail = None
        self.lru_size = 0
        self.capacity = capacity

    def get(self, key):
        if key in self.cache_map:
            cache_node = self.cache_map[key]
            if cache_node != self.lru_head:
                if cache_node == self.lru_tail:
                    self.lru_tail = cache_node.last
                    self.lru_tail.next = None
                else:
                    cache_node.last.next = cache_node.next
                    cache_node.next.last = cache_node.last
                self.lru_head.last = cache_node
                cache_node.next = self.lru_head
                cache_node.last = None
                self.lru_head = cache_node
            return cache_node.val
        return -1

    def put(self, key, value):
        if key in self.cache_map:
            self.cache_map[key].val = value
            self.get(key)
            return
        if self.lru_size == self.capacity:
            del self.cache_map[self.lru_tail.key]
            if self.lru_tail == self.lru_head:
                self.lru_tail = self.lru_head = None
            else:
                self.lru_tail = self.lru_tail.last
                self.lru_tail.next = None
            self.lru_size -= 1
        cache_node = LRUNode(key, value, next=self.lru_head)
        if self.lru_head is not None:
            self.lru_head.last = cache_node
            cache_node.next = self.lru_head
            self.lru_head = cache_node
        else:
            self.lru_head = self.lru_tail = cache_node
        self.cache_map[key] = cache_node
        self.lru_size += 1

# s = LRUCache(3)
# s.put(1, 1)
# s.put(2, 2)
# s.put(3, 3)
# s.put(4, 4)
# print(s.get(4))
# print(s.get(3))
# print(s.get(2))
# print(s.get(1))
# s.put(5, 5)
# print(s.get(1))
# print(s.get(2))
# print(s.get(3))
# print(s.get(4))
# print(s.get(5))

s = LRUCache(1)
s.put(2, 1)
print(s.get(2))
s.put(3, 2)
print(s.get(2))
print(s.get(3))