def missingNumber(nums: list[int]) -> int:
    nums.sort()

    if nums[-1] != len(nums):
        return len(nums)
    elif nums[0] != 0:
        return 0

    for i in range(1, len(nums)):
        expected_num = nums[i - 1] + 1
        if nums[i] != expected_num:
            return expected_num


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(missingNumber(nums))

    """


    KEY INSIGHT: 
    - first, take care of endopints - first and last elements (has to match 0 or the length of the array)
    - then, missing number has to be in [1,n)
    """
