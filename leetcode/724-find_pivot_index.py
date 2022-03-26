def pivotIndex(nums: list[int])->int:

    total_sum = sum(nums)

    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - (left_sum + nums[i])
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1

if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    print(pivotIndex(nums))


'''
KEY INSIGHT: 
- calculate total sum first
- realize that left sum has to equal right sum
- right sum is found by subtracting total sum from left sum and index
- left sum is added every iteration from left elements
'''