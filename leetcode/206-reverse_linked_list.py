class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: [ListNode]) -> [ListNode]:
    l = None
    r = head
    while r:
        next = r.next
        r.next = l
        l = r
        r = next
    return l


'''
KEY INSIGHT:
- use 2 pointer solution!
- use a temporary variable 'next' to store the intermediary step
- reversing linked list just means switching the pointers to face other way
'''