def counting_sort(unsorted: list[int]) -> list[int]:
    
    arr=unsorted[:]
    # 1. Find the maximum value
    max_val = max(arr)

    # 2. Create count array of size (max + 1)
    counts = [0] * (max_val + 1)

    # 3. Count occurrences
    for val in arr:
        counts[val] += 1

    # 4. Cumulative sum for correct index placing.
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # 5. Build output array (stable: go right to left)
    output = [0] * len(arr)
    for j in range(len(arr) - 1, -1, -1):
        val = arr[j]
        counts[val] -= 1
        output[counts[val]] = val

    return output

if __name__ == '__main__':
    print(counting_sort([6, 0, 0, 3, 4, 2, 1, 1, 6, 3, 3, 1, 2]))