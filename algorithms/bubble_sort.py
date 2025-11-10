def bubble_sort(data):
    n = len(data)
    while n > 1:
        new_n = 0
        for i in range(1, n):
            if data[i-1] > data[i]:
                data[i-1], data[i] = data[i], data[i-1]
                new_n = i
        n = new_n  # everything after new_n is already in place
    return data

if __name__ == "__main__":
    print(bubble_sort([7,6,4,5])) # -> [4, 5, 6, 7]