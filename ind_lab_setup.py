# Analysis and Optimisation Labs Starter Code
# Lab 1
import cProfile


# Inefficient version
def has_duplicates_slow(numbers: list[int]) -> bool:
    # Outer loop runs n times
    for i in range(len(numbers)):
        # Inner loop runs roughly n times in the worst case
        for j in range(i + 1, len(numbers)):
            # This comparison is O(1)
            if numbers[i] == numbers[j]:
                return True  # Total: n * n * 1 = O(n^2)
    return False
#Each loop through the list multiplies time complexity by its length
# Your fast version here
# Hint: Use membership testing
def has_duplicates_fast(numbers: list[int]) -> bool:
    """
    Looks up for duplicates using testing set membership.
    Loop through list has O(n) time-complexity, test membership
    in sets has O(1) time-complexity, similarly to adding a new element
    to the set.
    """
    #memory for seen numbers
    memo=set()
    # This loop is O(n)
    for num in numbers:
        #Test membership in sets is O(1)
        if num in memo:
            return True
        memo.add(num)
    return False
#print(has_duplicates_fast([1,2,3]), has_duplicates_fast([1,2,1]))
def find_pair(numbers:list[int], target:int)->bool:
    """
    Returns true if any pair of numbers from the list adds up to a target number.
    """
    seen = set()
    for num in numbers:
        #Test membership in sets is O(1)
        if target - num in seen:
            return True
        seen.add(num)
    return False

# Lab 3
# Which function is the bottleneck and why?
def create_lookup():
    return {i: i * i for i in range(5000)}


def process_items(items: range, lookup: dict[int, int]) -> list[int]:
    return [lookup.get(item, 0) for item in items]


def append_to_list(count: int) -> list[list[int]]:
    all_data: list[list[int]] = []
    for i in range(count):
        sub_list: list[int] = []
        for j in range(count):
            if i == j:
                sub_list.append(j)
        all_data.append(sub_list)
    return all_data


def main():
    all_data: list[list[int]] = append_to_list(5000)
    print(all_data[:30])
    lookup = create_lookup()
    process_items(range(100), lookup)


# Run the profiler https://docs.python.org/3/library/profile.html
