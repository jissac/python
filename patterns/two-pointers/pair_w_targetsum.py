'''
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.
'''

## two pointers
def pair_w_targetsum(arr: list[int], target_sum: int) -> list[int]:
    l = 0
    r = len(arr) -1

    while l < r:
        current_sum = arr[l] + arr[r]
        if current_sum == target_sum:
            return [l,r]
        if current_sum > target_sum:
            r -= 1
        else:
            l += 1
    return [-1,1]

# hash soln
def pair_w_targetsumHASH(arr: list[int], target_sum: int) -> list[int]:
    hash = {}
    for i,num in enumerate(arr):
        diff = target_sum - num
        if diff in hash:
            return [hash[diff],i]
        else:
            hash[num] = i
        
def main():
  print(pair_w_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_w_targetsum([2, 5, 9, 11], 11))
  print(pair_w_targetsumHASH([2, 5, 9, 11], 11))
  print(pair_w_targetsumHASH([1, 2, 3, 4, 6], 6))

main()