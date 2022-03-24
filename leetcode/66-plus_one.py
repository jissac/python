def plusOne(digits: list[int])->list[int]:
    input = ''
    output = []
    for num in digits:
        input = input+str(num)
    plus_one = int(input) + 1
    for char in str(plus_one):
        output.append(int(char))
    return output

if __name__ == "__main__":
    nums =  [1,2,3]
    print(plusOne(nums))

'''
KEY INSIGHT: 
- conversion from string to int and vice versa
'''