'''
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
'''
def remove_duplicates(arr: list[int])-> int:
    hash ={}
    for _, num in enumerate(arr):
        if num in hash:
            hash[num] += 1
            arr.remove(num)
        else:
            hash[num] = 1
    return len(hash)

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()

'''
KEY INSIGHT:
- arr.remove() to remove element from array
- hash map!
- can't add one to an empty hash map (adding to null) have to initialize with 1 first
'''