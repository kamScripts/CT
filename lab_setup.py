"""This is your group lab setup file. 
We should start using type hints whenever possible going 
forward to tighten up our code.
e.g.,
def my_function(x: int) -> int:
    return x + 1

x: int  # type hint for variable x
-> int  # type hint for return value
-> int | None  # type hint for return value that can be int or None
You can use type hints for function arguments, return values, and variables.
"""

import timeit
import matplotlib.pyplot as plt


def time_operation(stmt: str, setup_template: str, sizes: list[int]) -> list[float]:
    """A helper function to time an operation for various list sizes."""
    times: list[float] = []
    for n in sizes:
        setup_code = setup_template.format(n=n)
        t = timeit.timeit(stmt, setup=setup_code,
                        number=100, globals=globals())
        times.append(t)
    return times


list_sizes: list[int] = [i * 100 for i in range(1, 20)]

stmt_1: str = 'my_list.pop()'
setup_1: str = 'import random; my_list = list(range({n}))'
times_1: list[float] = time_operation(stmt_1, setup_1, list_sizes)
label_1: str = 'pop() - O(1)'

stmt_2: str = 'my_list.pop(0)'
setup_2: str = 'import random; my_list = list(range({n}))'
times_2: list[float] = time_operation(stmt_2, setup_2, list_sizes)
label_2: str = 'pop(0) - O(n)'


# --- PLOTTING ---
plt.plot(list_sizes, times_1, 'o-', label=label_1)
plt.plot(list_sizes, times_2, 'o-', label=label_2)
plt.xlabel("List Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()
