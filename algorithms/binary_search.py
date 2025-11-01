def binary_search(data,target, low, high):
    """Example from Goodrich et al. Data Structures & Algorithms"""
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1,high)
        
def b_search(data:list[int], target:int)->int:
    """
    Binary search O(log n) working on sorted list
    data: sorted [int]
    target: int
    
    returns: index of a target
    """
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == '__main__':

    dt=[0,5,10,15,20,30]
    
    print(binary_search(dt,20,0,len(dt)-1))
    print(b_search(dt,10))