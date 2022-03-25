class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## METHOD 1: USE HASH MAP
def getIntersectionNode(headA:ListNode, headB:ListNode) -> ListNode:
    setB = set()
    while headB != None:
        setB.add(headB)
        headB = headB.next
    while headA != None:
        if headA in setB:
            return headA
        headA = headA.next
    return None


## METHOD 2: USE 2 POINTERS
def getIntersectionNode2(headA:ListNode, headB:ListNode) -> ListNode:


'''
KEY INSIGHT: 
- create a set with one linked list first, then compare the other linked list to find intersection
'''