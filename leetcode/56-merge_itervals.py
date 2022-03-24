def merge(intervals: [[int]]) -> [[int]]:
    intervals.sort(key=lambda x: x[0])
    # print(intervals)
    output = [intervals[0]]

    for start, end in intervals[1:]:
        prevEnd = output[-1][1]
        if start <= prevEnd:
            # print(prevEnd, start,end)
            output[-1][1] = max(prevEnd, end)
            print(output)
        else:
            output.append([start, end])
    return output


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    out = merge(intervals)
    print(out)


"""
KEY CONCEPTS: 
- sort with lambda in Python (line 4) : https://docs.python.org/3/howto/sorting.html
- 2d array [-1][i] returns the last array's ith element in the 2d array
- max(prevEnd,end) needed to take the longest length from second index
TIME COMPLEXITY:
O(nlogn) b/c sort the array
SPACE COMPLEXITY: 
O(n)
"""
