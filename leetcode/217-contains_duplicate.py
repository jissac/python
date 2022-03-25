def containsDuplicate(nums: list[int]) -> bool:
    hash = {}
    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    print(hash.keys())
    if max(hash.values()) >= 2:
        return True
    return False


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3]
    print(containsDuplicate(nums))

    """
KEY INSIGHT: 
- hash maps!!!!!
- hash.values() returns array of values in hashmap
- hash.keys() returns array of keys in hashmap
"""
