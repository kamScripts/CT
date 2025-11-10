def selection_sort(data: list[int]) ->list[int]:
    n = len(data)
    for i in range(n - 1):
        # Assume the current index has the smallest element
        min_idx = i
        # Find the index of the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data


if __name__ == "__main__":
    print(selection_sort([7, 6, 4, 5]))    # -> [4, 5, 6, 7]

