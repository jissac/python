def findMaxConsecutiveOnes(nums: list[int])-> int:
    
    ones_count = 0
    max_ones = 0
    for i in range(len(nums)):
        # print(i,ones_count,max_ones)
        if nums[i]:
            ones_count += 1
            max_ones = max(max_ones,ones_count)
        else: 
            
            ones_count = 0

    return max_ones 

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(nums))

'''
KEY INSIGHT: 
- keep a count of 1s encountered, reset count to 0 whenever we encounter anything not 1 (0)
- this is making count of 1s between zeros instead of contguous 1s (same thing)
- take max of the ones count
'''