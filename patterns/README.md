## Patterns

### Sliding window
- when dealing with an array (or linked list) and want to find/calculate something among all the subarrays or sublists of a given size
- dealing with **contiguous** elements

### Two pointers
- when dealing with **sorted** arrays (or linked lists) and need to find a set of elements that fulfill certain constraints

## Fast and slow pointers
- The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.
- By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.