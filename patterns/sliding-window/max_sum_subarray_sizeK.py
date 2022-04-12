'''
PROBLEM: 
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.

'''

## SLIDING WINDOW
def max_sub_array_of_size_k(k: int, arr: list[int]) -> int:
    max_sum, window_sum = 0,0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


def main():
  k = 3
  arr = [2, 1, 5, 1, 3, 2]
  result = max_sub_array_of_size_k(k,arr)
  print(result)

main()

'''
KEY INSIGHT: 
- create variables, window_start, max_sum and window_sum
- iterate thru array and add to window sum
- conditional to check if window size is reached, do calculations inside conditional
'''