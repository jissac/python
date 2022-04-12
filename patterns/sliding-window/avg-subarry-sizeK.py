'''
PROBLEM: 
Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

'''
## BRUTE FORCE
def find_averages_of_subarrays(k: int, arr: list[int]) -> list[int]:
    output = []
    for i in range(len(arr)-k+1):
        sum = 0
        for j in range(i,i+k):
            sum += arr[j]
        output.append(sum/k)
    return output

## SLIDING WINDOW
def find_avg_of_subarrays_window(k: int, arr: list[int]) -> list[int]:
    output = []
    window_sum, window_start = 0,0

    for window_end in range(len(arr)):
        # print(window_end)
        window_sum += arr[window_end] # add next element
        # print(window_sum)

        if window_end >= k - 1:
            output.append(window_sum/k)
            window_sum -= arr[window_start] # subtract element going out
            window_start += 1 # slide window ahead
    return output


def main():
  k = 5
  arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
  result = find_averages_of_subarrays(k, arr)
  print("Averages of subarrays of size K: " + str(result))
  print(find_avg_of_subarrays_window(k,arr))


main()

'''
KEY INSIGHT:
- calculate sum of entire array in loop, limit it by window size using a conditional
- in the condition, do avg calc, remove first element and slide window forward, new element will be added in main for loop

'''