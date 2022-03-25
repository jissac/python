def moveZeros(nums: list[int]):
    zeros = []
    nonzeros = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros.append(nums[i])
        else: 
            nonzeros.append(nums[i])
    print(nonzeros,zeros)
    for i in range(len(nonzeros)):
        print(i)
        nums[i] = nonzeros[i]

    for i in range(len(nonzeros),len(nums)):
        print(i)
        nums[i] = 0
    return nums

# second way using two pointers
def moveZeros2(nums: list[int]):
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
    return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    # print(moveZeros(nums))
    print(moveZeros2(nums))

'''

KEY INSIGHT: using two pointers greatly smiplifies code

'''