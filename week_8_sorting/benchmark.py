import timeit
import data_generators
from merge_sort import merge_sort
from insertion_sort import insertion_sort

sort_func=merge_sort
generator_func=data_generators.randomize_list

def benchmark_sort(
    n_min: int,
    n_max: int,
    step: int,
    output_path: str = "benchmark_results.txt",
    trials: int = 1
) -> None:
    """
    Benchmarks a sorting function using a data generator over a range of input sizes.

    Parameters:
    - sort_func: callable, the sorting algorithm to benchmark
    - generator_func: callable, generates input data for sorting
    - n_min: int, starting input size
    - n_max: int, ending input size (exclusive)
    - step: int, increment between input sizes
    - output_path: str, file path to save results
    - trials: int, number of repetitions per input size
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("n,time_seconds\n")
        for n in range(n_min, n_max, step):
            setup_code = f"from __main__ import sort_func, generator_func; arr = generator_func({n})"
            stmt = "sort_func(arr)"
            t = timeit.timeit(stmt=stmt, setup=setup_code, number=trials, globals=globals())
            f.write(f"{n},{t:.6f}\n")
            #print(f"n={n}, time={t:.6f}s")

# Example usage
if __name__ == "__main__":
    
    benchmark_sort(
        n_min=100,
        n_max=20600,
        step=500,
        output_path="./week_8_sorting/merge_sort_benchmark.txt",
        trials=1
    )