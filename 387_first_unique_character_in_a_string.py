class Node:
    def __init__(self, char, index):
        self.char = char
        self.index = index
        self.next = None
        self.count = 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}

        i = 0
        l = len(s)
        head = Node(None, None)
        current = head
        while i < l:
            if s[i] not in h:
                current.next = Node(s[i], i)
                h[s[i]] = current.next
                current = current.next
            else:
                node = h[s[i]]
                node.count = node.count + 1
            i = i + 1

        node = head
        while True:
            node = node.next
            if node is None:
                return -1
            if node.count == 1:
                return node.index
            if node.next is None:
                break
        return -1

print(Solution().firstUniqChar(""))
#print(Solution().firstUniqChar("leetcode"))
#print(Solution().firstUniqChar("loveleetcode"))
