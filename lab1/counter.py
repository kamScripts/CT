import time
t=time.time()
def timer(func, *args):
    start=t
    func(*args)
    stop=t
    print(f"{func.__name__} Execution time: {round((stop-start)*1000, 6)} ms.")
