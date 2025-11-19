import matplotlib.pyplot as plt
import numpy as np
import random


def multi_visualize_sort(algorithms, delay=0.05):
    """
    Visualizes multiple sorting algorithms side by side in one matplotlib window.
    
    Parameters:
        algorithms: list of tuples (title, generator_func, data)
        delay: pause duration between frames
    """
    n = len(algorithms)
    fig, axes = plt.subplots(1, n, figsize=(6 * n, 5))
    fig.suptitle("Sorting Algorithm Comparison")

    if n == 1:
        axes = [axes]  # ensure axes is always a list

    bars = []
    generators = []

    colors = ['skyblue', 'salmon', 'lightgreen', 'violet', 'orange', 'gold', 'turquoise']  # extend as needed
    
    for idx, (ax, (title, gen_func, data)) in enumerate(zip(axes, algorithms)):
        x = np.arange(len(data))
        color = colors[idx % len(colors)]  # cycle if more algorithms than colors
        bar = ax.bar(x, data, align="center", color=color)
        ax.set_title(title)
        bars.append(bar)
        generators.append(gen_func(data.copy()))


    while True:
        active = False
        for bar_rects, gen in zip(bars, generators):
            try:
                step = next(gen)
                for rect, h in zip(bar_rects, step):
                    rect.set_height(h)
                active = True
            except StopIteration:
                continue
        plt.pause(delay)
        if not active:
            break

    for ax in axes:
        ax.set_title(ax.get_title() + " - Done")
    plt.show()

def dual_visualize_sort(gen1, gen2, data1, data2, delay=0.05):
    """
    Visualizes two sorting algorithms side by side in a single matplotlib window.
    
    Parameters:
        gen1, gen2: generator functions for sorting (yielding list states)
        data1, data2: initial data for each algorithm
        delay: pause between frames
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Sorting Algorithm Comparison")

    x = np.arange(len(data1))
    bars1 = ax1.bar(x, data1, color='skyblue')
    bars2 = ax2.bar(x, data2, color='salmon')

    ax1.set_title("Merge Sort")
    ax2.set_title("Insertion Sort")

    gen1 = gen1(data1.copy())
    gen2 = gen2(data2.copy())

    while True:
        try:
            step1 = next(gen1)
            for rect, h in zip(bars1, step1):
                rect.set_height(h)
        except StopIteration:
            pass

        try:
            step2 = next(gen2)
            for rect, h in zip(bars2, step2):
                rect.set_height(h)
        except StopIteration:
            pass

        plt.pause(delay)

        # Stop when both generators are exhausted
        if 'step1' not in locals() and 'step2' not in locals():
            break

    ax1.set_title("Merge Sort - Done")
    ax2.set_title("Insertion Sort - Done")
    plt.show()

def visualize_sort(sort_func, data, delay=0.05, title="Sorting Visualization"):
    """
    Visualizes a sorting algorithm using matplotlib animation.
    
    Parameters:
        sort_func: generator-based sorting function yielding list states
        data: list of values to sort
        delay: time (in seconds) between frames
        title: title for the plot window
    """
    x = np.arange(len(data))  # x-axis positions for bars
    fig, ax = plt.subplots()
    bar_rects = ax.bar(x, data, align="center")  # initial bar chart
    ax.set_title(title)

    # Animate each step yielded by the sorting generator
    for step in sort_func(data.copy()):
        for rect, h in zip(bar_rects, step):
            rect.set_height(h)  # update bar height
        plt.pause(delay)  # brief pause to render frame

    # Final sorted state
    for rect, h in zip(bar_rects, step):
        rect.set_height(h)
    ax.set_title("Sorted!")
    plt.show()

def insertion_sort_gen(A):
    """
    Generator-based insertion sort.
    Yields the list state after each change for visualization.
    """
    for k in range(1, len(A)):
        current = A[k]
        j = k
        while j > 0 and A[j - 1] > current:
            A[j] = A[j - 1]  # shift element right
            j -= 1
            yield A.copy()  # yield intermediate state
        A[j] = current
        yield A.copy()  # yield after insertion
     
def merge_sort(S):
    """Sort the elements of list S using the merge-sort algorithm."""
    def merge(S1, S2,S):
        """Merge two sorted lists S1 and S2 into properly sized list S."""
        i=j=0
        while i + j <len(S):
            if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
                S[i+j] = S1[i]  #copy i-th element of S1 as next item of S
                i += 1
            else:
                S[i+j] = S2[j]
                j += 1          #copy j-th element of S2 as next item of S
    n = len(S)
    if n < 2:
        return  #list is already sorted
    #divide
    mid = n // 2
    S1 = S[0:mid]   #copy 1st half
    S2 = S[mid:n]   #copy 2nd half
    #conquer (with recursion)
    merge_sort(S1)  #sort copy of first half
    merge_sort(S2)  #sort copy of second half
    # merge results
    merge(S1,S2,S)

def merge_gen(S1, S2, S):
    """
    Generator-based merge function.
    Merges sorted lists S1 and S2 into S, yielding after each write.
    """
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1
        yield S  # yield after each merge step

def merge_sort_gen(S):
    """
    Generator-based merge sort.
    Yields the list after each merge step for visualization.
    """
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]

    # Recursively sort both halves
    yield from merge_sort_gen(S1)
    yield from merge_sort_gen(S2)

    # Merge sorted halves into S
    merge_gen_instance = merge_gen(S1, S2, S)
    for _ in merge_gen_instance:
        yield S  
        
def bubble_sort_gen(data):
    """
    Generator-based bubble sort.
    Yields the list after each swap for visualization.
    """
    n = len(data)
    while n > 1:
        new_n = 0
        for i in range(1, n):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                new_n = i
                yield data.copy()  # yield after each swap
        n = new_n


def counting_sort_gen(arr: list[int]):
    """
    Generator-based counting sort.
    Sorts in-place and yields the list after each placement into arr.
    """
    max_val = max(arr)
    counts = [0] * (max_val + 1)

    # Count occurrences
    for val in arr:
        counts[val] += 1

    # Cumulative sum
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # Build output and reflect changes in arr
    output = [0] * len(arr)
    for j in range(len(arr) - 1, -1, -1):
        val = arr[j]
        counts[val] -= 1
        output[counts[val]] = val
        yield output
lst= [x for x in range(1,100,2)]
lst2=np.random.randint(1,100,50)
random.shuffle(lst)
#dual_visualize_sort(merge_sort_gen, insertion_sort_gen, lst, lst.copy())


multi_visualize_sort([
    ("Merge Sort", merge_sort_gen, lst),
    ("Insertion Sort", insertion_sort_gen, lst.copy()),
    ("Bubble Sort", bubble_sort_gen, lst.copy()),
    ("Counting Sort", counting_sort_gen, lst.copy())
], delay=0.03)
