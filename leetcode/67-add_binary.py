def addBinary(a: str, b: str)-> str:
    out = ''
    carry = 0

    a,b = a[::-1], b[::-1]

    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0

        total = digitA + digitB + carry    
        out = str(total % 2) + out
        # print('out',out,total%2)
        carry = total // 2
        # print(digitA,digitB,total,out,carry)

    if carry: 
        out = str(carry) + out
    return out
    
if __name__ == '__main__':
    a = '11'
    b = '1'
    print(addBinary(a,b))

'''
KEY INSIGHT: 
- reverse the strings to add right to left a[::-1]
- create var for carry 
- convert to int and then add, % and // operators come in handy
- dont forget carry at the very end 
'''