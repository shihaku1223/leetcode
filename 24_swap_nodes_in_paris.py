# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swap(self, pre, x, y):
        pre.next = y
        temp = y.next
        y.next = x
        x.next = temp

    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = ListNode()
        dummy.next = head
        current = dummy
        pre = dummy
        count = 0
        while True:
            count = count + 1
            if count % 2 == 0:
                temp = current.next
                self.swap(pre, current, current.next)
                current = temp
            else:
                pre = current
            if current.next is None:
                break
            current = current.next
        return dummy.next



dummy = ListNode()
head = ListNode(1)
dummy.next = head
current = head
i = 2
while i <= 4:
    node = ListNode(i)
    current.next = node
    current = node
    i = i + 1

current = Solution().swapPairs(head)
while True:
    print(current.val)
    if current.next is None:
        break
    current = current.next
