
def merge_sort(data: list[int]) -> list[int]:
    """
    Return a new list containing data sorted in ascending order (not in-place).
    """
    n = len(data)
    if n <= 1:
        # Return a shallow copy to avoid mutation
        return data[:]

    mid = n // 2
    left_sorted = merge_sort(data[:mid])
    right_sorted = merge_sort(data[mid:])
    return _merge(left_sorted, right_sorted)


def _merge(left: list[int], right: list[int]) -> list[int]:
    i = j = 0
    merged: list[int] = []

    while i < len(left) and j < len(right):
        # Use <= to ensure stability: when equal, take from left first
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # One of the lists may have remaining items
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    return merged


if __name__ == "__main__":
    print(merge_sort([7, 6, 4, 5]))      # -> [4, 5, 6, 7]

