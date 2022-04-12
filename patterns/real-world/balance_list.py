'''
given a list, balance it like so:
[1,1,2] -> {2:1}
[1,1,1,5,3,2,2] -> {5:2,3:2,2:1}
'''

def balance_list(nums: list[int])-> dict:
    counts = {}
    for i,num in enumerate(nums):
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    res = {}

    max_value = max(counts.values())
    print(max_value)
    for key, val in counts.items():
        print(key,val)
        if val - max_value != 0:
            res[key] = max_value-val
    return res

def main():
    nums = [1,1,1,5,3,2,2] 
    print(balance_list(nums))

main()