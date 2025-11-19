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
   

if __name__=='__main__':

    #print(reverse_string('software development'))
    #print(recursive_palindrome('racecar'))
    #print(sumList([1,2,3,4]), sumList([x for x in range(100)]), sep='\t')
    #print(factorial(5), 1*2*3*4*5)
    print(find_n_fibo(12))