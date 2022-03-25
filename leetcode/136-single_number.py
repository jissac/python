def singleNumber(nums: list[int]) -> int:
    hash = {}
    for i, num in enumerate(nums):
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    return min(hash, key=hash.get)


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3]
    print(singleNumber(nums))


"""
KEY INSIGHT: 
- hash maps!!!!!
"""
