def majorityElement(nums: list[int]) -> int:
    majority = len(nums) // 2
    hmap = {}
    for i, num in enumerate(nums):
        if num in hmap:
            hmap[num] += 1
        else:
            hmap[num] = 1
    return max(hmap, key=hmap.get)


if __name__ == "__main__":
    nums = [3, 2, 3, 2, 2, 2]
    print(majorityElement(nums))

"""
KEY INSIGHT: 
- WRITE OUT THE PROBLEM AND SOLN IN WORDS BEFORE SOLVING
- above step will simplify whole process
- max(hmap, key = ) to get the max value by key!
"""
