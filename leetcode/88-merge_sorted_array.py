def merge(nums1: list[int], nums2: list[int], m: int, n: int):
    if len(nums1) != m + n:
        nums1.extend(nums2)

    for i in range(n):
        print(i)
        nums1[m + i] = nums2[i]
    nums1.sort()
    return nums1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    print(merge(nums1, nums2, m, n))

"""
KEY INSIGHT: 
- extend and built in sort fn
- more efficient ways to solve problem but this is straightforward
"""
