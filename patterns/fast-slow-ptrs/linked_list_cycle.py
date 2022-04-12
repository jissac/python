'''
Given the head of a Singly LinkedList, 
write a function to determine if the LinkedList has a cycle in it or not.
'''

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

## two pointers (fast and slow)
def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


## set
def has_cycle_set(head: Node) -> bool:
    s = set()
    while head:
        if head in s:
            return True
        else:
            s.add(head)
            head = head.next
    return False


'''
KEY INSIGHT: 
- fast and slow ptrs
- in while loop have to check fast and fast.next != None
'''

##############
'''
Given the head of a LinkedList with a cycle, find the length of the cycle.
'''

def find_cycle_length(head: Node)-> int:
    slow, fast = head,head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast: # found the cycle
            return calculate_cycle_length(slow)
    return 0

def calculate_cycle_length(slow: Node)-> int:
    current = slow
    cycle_length = 0
    while current:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


'''
KEY INSIGHT: 
- use the above solution to find the cycle in the LinkedList. 
Once the fast and slow pointers meet, we can save the slow pointer 
and iterate the whole cycle with another pointer until we see the 
slow pointer again to find the length of the cycle.
'''