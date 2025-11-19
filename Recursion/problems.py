def reverse_string(s:str)-> str:
    """Reverse a string recursively."""
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

def recursive_palindrome(s:str)->bool:
    """Return True if string is palindrome."""
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive_palindrome(s[1:-1])

def sumList(lst: list[int | float]) -> int | float | None:
    """Sum numerical elements of a list"""
    try:
        if len(lst)==1:
            return lst[0]
        return lst[0] + sumList(lst[1:]) # type: ignore
    except ValueError:
        return None
def factorial(num:int)->int:
    """Find factorial of a number."""
    return num * factorial(num-1) if num >1 else num
def find_n_fibo(num:int)->int:
    """Find n-th number of Fibonacci Sequence"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return find_n_fibo(num-1) + find_n_fibo(num-2)
def fibonacci_fast(num:int)->int|None:
    """Function based on example from "Think Python: How to Think Like Computer Scientist"
       by Allen Downey (2015). Green Tea Press.
       To find nth number of a sequence function need to be called recursively twice
       What's very quickly increase call stack exponentially. Solution to this problem
       is memoization. Computed result are stored in dictionary located in outer function.
       Inner function checks first if number of a sequence is in dict and return
       element straight away else  compute and update dict. This technique reduces number of
       recursive calls significantly.
       Naive version has time complexity of O(2**n) as each call creates two recursive calls
       creating a binary tree of calls with exponential growth.
       Optimized Recursive version with memoization uses dictionary to store already computed
       values, avoiding redundant calculations and runs in worst-case scenario in O(n).
       Each Fibonacci number from 0 to n is computed only once. Recursive calls reuse the result
       instead of computing it again and again 
       
       
       """
    memo={0:0,1:1}
    def fibo_inner(num):
        if num in memo:
            return memo[num]
        memo[num] = fibo_inner(num-1)+fibo_inner(num-2)
        return memo[num]
    return fibo_inner(num)
def fibonacci_matrix(n: int) -> int:
    """Compute the n-th Fibonacci number using matrix exponentiation (O(log n) time).
       Version created by Microsoft Copilot."""
    def matrix_mult(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0],
             A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0],
             A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def matrix_pow(matrix, power):
        result = [[1, 0], [0, 1]]  # Identity matrix
        while power > 0:
            if power % 2 == 1:
                result = matrix_mult(result, matrix)
            matrix = matrix_mult(matrix, matrix)
            power //= 2
        return result

    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = matrix_pow(base, n - 1)
    return result[0][0]
if __name__=='__main__':

    #print(reverse_string('software development'))
    #print(recursive_palindrome('racecar'))
    #print(sumList([1,2,3,4]), sumList([x for x in range(100)]), sep='\t')
    #print(factorial(5), 1*2*3*4*5)
    print(fibonacci_fast(120))