def generate(numRows: int):
    res = [[1]]
    for i in range(1,numRows):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res

if __name__ == "__main__":
    numRows = 4
    print(generate(numRows))

"""
KEY INSIGHT: 

"""
