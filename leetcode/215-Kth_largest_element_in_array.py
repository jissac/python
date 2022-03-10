def findKthLargest(nums:[int],k: int)->int:
    new_nums = sorted([i for i in nums],reverse=True)
    return new_nums[k-1]

if __name__ == '__main__':
    nums = [7,1,5,4,6,4]
    out = findKthLargest(nums,1)
    print(out)
