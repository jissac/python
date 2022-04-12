'''
Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum 
is greater than or equal to ‘S’. Return 0 if no such subarray exists.
'''
def smallest_subarray_sum(s: int, arr: list[int]) -> int:
    window_sum = 0
    window_size = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        window_size += 1 
        while window_sum > s:
            window_sum -=  arr[i]
            window_size -= 1