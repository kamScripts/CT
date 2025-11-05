def insertion_sort(A):
    """
    Example from Goodrich et al. Data Structures & Algorithms(2013)
    Sort list of comparable elements into non-decreasing order.
    """
    for k in range(1, len(A)): #from 1 to n-1
        current = A[k] #current element to be inserted
        j=k #find correct index for current
        while j>0 and A[j-1]>current:#element A[j-1] must be after current
            A[j]=A[j-1]
            j-=1
        A[j]=current #current el in the right place
        
if __name__=="__main__":
    lst=[4,1,4,5,2,9]
    insertion_sort(lst)
    print(lst)