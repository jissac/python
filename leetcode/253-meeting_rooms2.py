def minMeetingRooms(intervals: [[int]]) -> int:
    count = 0
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    s, e, count, result = 0, 0, 0, 0

    while s < len(start_times):
        if start_times[s] < end_times[e]:
            count += 1
            s += 1
        else:
            e += 1
            count -= 1
        result = max(result, count)
    return result


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [10, 15], [9, 15]]
    out = minMeetingRooms(intervals)
    print(out)


"""
KEY CONCEPTS: 
- sorted() function
- two separate arrays for start and end
- two separate pointers for start and end arrays and compare min
- if min is in start array, increment count and shift right in start array
- if tie, end first, and decrement count


TIME COMPLEXITY:
O(nlogn) b/c sort the array
SPACE COMPLEXITY: 
O(n)
"""
