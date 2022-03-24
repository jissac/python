def removeDuplicates(nums: list[int]) -> int:
    ptr = 0
    if len(nums) == 0:
        return ptr
    for i in range(1, len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[ptr] = nums[i + 1]
            ptr += 1
    return ptr


if __name__ == "__main__":
    nums = [1, 1, 2]

    print(removeDuplicates(nums))
