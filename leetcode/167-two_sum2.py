def twoSum(numbers: list[int], target: int)->list[int]:
    r = 1
    for i in range(len(numbers)):
        print(i,r)
        for j in range(r,len(numbers)):
            sum = numbers[i] + numbers[j]
            print(sum, i, j)
            if sum == target:
                return [i+1, j+1]
        r += 1

## BETTER METHOD, FASTER
def twoSum2(numbers: list[int], target: int)->list[int]:
    l = 0
    r = len(numbers)-1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l+1, r+1]
        elif sum < target:
            l += 1
        elif sum > target:
            r -= 1
    return [-1,-1]


if __name__ == '__main__':
    numbers = [2,3,4]
    target = 7
    print(twoSum2(numbers,target))
    

'''
KEY INSIGHT:
- two pointer soln
- instead of just moving l++ and r-- every iteration, check the sum
- if the sum is > target, move left up since array is sorted
- if the sum is < target, move right down since array is sorted
'''