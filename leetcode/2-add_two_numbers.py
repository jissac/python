class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1,l2):
    dummy = ListNode()
    cur = dummy

    while l1 or l2: