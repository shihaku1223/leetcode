# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode()
        current = head
        p = l1
        q = l2
        carry = 0

        while(p is not None or q is not None):
            a = p.val if p is not None else 0
            b = q.val if q is not None else 0
            sum = a + b + carry
            node = ListNode(sum % 10)
            carry = int(sum / 10)
            current.next = node
            current = current.next            
            
            if(p is not None):
                p = p.next
            if(q is not None):
                q = q.next

        if(carry != 0):
            current.next = ListNode(1)
        return head.next

if __name__ == "__main__":
    sol =  Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = sol.addTwoNumbers(l1, l2)
    curr = result
    while(curr is not None):
        print(curr.val)
        curr = curr.next
