'''
Given the head of a Singly LinkedList that contains a cycle, 
write a function to find the starting node of the cycle.

'''

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_cycle_start(head: Node) -> Node:
    s = set()
    current = head
    while current:
        if current in s:
            return current
        else:
            set.add(current)
            current = current.next

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
