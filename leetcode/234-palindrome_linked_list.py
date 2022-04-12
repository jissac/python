class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head:[ListNode]) -> bool:
    p = []
    while head:
        p.append(head.val)
        head = head.next
    l = 0
    r = len(p) -1
    while l < r:
        if p[l] == p[r]:
            l += 1
            r -= 1
        else:
            return False

    return True


'''
KEY INSIGHT:

- start somewhere, as you solve bit by bit, the entire problem soln unfolds
- creaet array to store node values, then compare using left and right pointer
'''