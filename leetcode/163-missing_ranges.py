def findMissingRanges(nums: list[int],lower:int, upper:int)-> list[str]:
    def array_format(lower,upper):
        if lower == upper:
            return str(lower)
        return str(lower) + '->' + str(upper)
    output = []

    if len(nums) == 0: 
        output.append(array_format(lower, upper))
        return output
    diff_lower = nums[0] - lower
    diff_upper = upper - nums[-1] 
    print(diff_lower, diff_upper)
    if diff_lower != 0:
        output.append(array_format(lower, nums[0]-1))
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        print(diff)
        if diff != 1:
            output.append(array_format(nums[i]+1, nums[i+1]-1))
    if diff_upper !=0:
        output.append(array_format(nums[-1]+1,upper))
    return output


if __name__ == "__main__":
    nums =  []
    lower = 1
    upper = 1
    print(findMissingRanges(nums,lower,upper))

    '''
KEY INSIGHT: 
- write down prob and soln first on paper in words
- work out the edge cases first, then iterate through array
    '''