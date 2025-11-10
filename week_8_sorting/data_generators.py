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
def randomize_list(n:int)->list[int]:
    """Randomize sequence of integers from 1 to n
    using Fisher-Yates shuffle aLgorithm"""
    
    arr=[num for num in range(1,n+1)]
    for i in range(n-1,0,-1):
        j=random.randint(0,i)
        arr[i],arr[j]=arr[j],arr[i]
    return arr

def get_nearly_sorted(n:int)->tuple:
    """Returns list of  nearly sorted integers (~5% randomized)"""

    arr=[num for num in range(1,n+1)]
    indices_swapped = set()
    i,j=0,0
    for _ in range(int(n*0.05)):
        while i == j or i in indices_swapped or j in indices_swapped:
            i,j=random.randint(0,n-1),random.randint(0,n-1)
        arr[i],arr[j]=arr[j],arr[i]
        indices_swapped.add(i)
        indices_swapped.add(j)

    return indices_swapped,arr
def get_reversed_list(n:int)->list[int]:
    """
    Returns a list n integers in descending order"""
    return [i for i in range(n,0,-1)]
if __name__=='__main__':
    
    #arr = randomize_list(10000)
    #for _ in range(1000):
    #    arr = get_nearly_sorted(100)
    #    print(arr[0],len(arr[0]),arr[1],sep='\n')
    arr = [x for x in range(500)]
    arr=get_reversed_list(20)
    print(arr)