def factorial(num: int, memo={1: 1}) -> int:
    """Find factorial of a number using recursion with memoization."""
    if num in memo:
        return memo[num]
    memo[num] = num * factorial(num - 1, memo)
    print(memo)
    return memo[num]
print(factorial(5))