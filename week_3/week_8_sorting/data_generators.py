import random
def get_random_list(n):
    taken_indices = set()
    nums = (i for i in range(1,n+1))
    i = 0
    arr=[None]*n
    for num in nums:
        while i in taken_indices:
            i = random.randint(1,n-1)
        arr[i]=num
        taken_indices.add(i)
    return arr
def randomize_list(n):
    """Randomize sequence of integers from 1 to n
    using Fisher-Yates shuffle aLgorithm"""
    arr=[num for num in range(1,n+1)]
    for i in range(n-1,0,-1):
        j=random.randint(0,i)
        arr[i],arr[j]=arr[j],arr[i]
    return arr
if __name__=='__main__':
    
    arr = randomize_list(1000000)
    print(arr)