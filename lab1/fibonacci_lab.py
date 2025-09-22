#a global var to count the number of function calls
count=0
memory={1:1,2:1}
def fib(n):
    """
    Calculates the nth num of Fibo sequence using a naive recursive approach
    """
    global count
    count+=1
    #Base Case: The condition that stops a recursive call
    #For Fibonacci, we know the 1st and 2nd nums are both 1
    if n<=2:
        return 1
    
    #Recursive Step: The function calls itself till base case is met.
    return fib(n-1)+fib(n-2)
def memoised_fib(n):
    """
    Calculates the nth Fibonacci number using recursion with memoisation.
    """
    global count
    count+=1
    
    #1. Check the cache first!
    if n in memory:
        return memory[n]
    #2. If not int cache, compute it, store it, then return
    res=memoised_fib(n-1)+memoised_fib(n-2)
    memory[n]=res
    return res

if __name__ == "__main__":
    nums = (i for i in range(20,35+1,5))
    counts=[[],[]]
    for num in nums:
        #return a tuple (n, nth number, calls)
        res=memoised_fib(num)
        counts[1].append((num,res,count))
        count=0
        res=fib(num)
        counts[0].append((num,res,count))
        count=0
    first_row=""    
    second_row="NAIVE    : "
    third_row="MEMOISED : "
    first_row+=" "*len(third_row)
    print("APPROACH", "COUNT OF CALLS", "TIME COMPLEXITY", sep="\t   ")    
    for n in counts[0]:
        first_row+=f"  n={n[0]} "
    
    print(first_row)
    for n in counts[0]:
        second_row+=f"{n[2]} "
    second_row+="  O(2**n)"
    print(second_row)
    for n in counts[1]:
        third_row+=f"  {n[2]}  "
    third_row+="        O(n)"
    print(third_row)
    
    
        