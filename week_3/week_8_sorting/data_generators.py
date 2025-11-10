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

if __name__=='__main__':
    
    arr = get_random_list(10000)
    print(arr)