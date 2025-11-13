import matplotlib.pyplot as plt


def reader(path:str)->list[list]:
    """Reads tests results and save in a list (n, time)"""
    with open(path, 'r', encoding='UTF-8') as file:
        coordinates= [[],[]]
        file.readline()
        for line in file:
            line = line.strip('\n')
            input_size, running_time = line.split(',')
            coordinates[0].append((float(input_size)))
            coordinates[1].append((float(running_time)))
        return coordinates
merge_results=reader('./week_8_sorting/merge_sort_benchmark.txt')
insertion_results=reader('./week_8_sorting/insertion_sort_benchmark.txt')
print(merge_results)
fig, ax = plt.subplots()
ax.plot(merge_results[0], merge_results[1], label='Merge Sort')
ax.plot(insertion_results[0], insertion_results[1], label='Insertion Sort')
ax.set_yscale('linear')
ax.grid(True)
plt.legend()
plt.show()