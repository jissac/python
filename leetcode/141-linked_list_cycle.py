class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    s = set()
    current = head
    while (current != None):
        if (current in s):
            return True
        s.add(current)
        current = current.next
        
    return False



'''
KEY INSIGHT: 
- set is used to store distinct elements
'''