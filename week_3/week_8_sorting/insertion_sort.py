import random

def insertion_sort(arr:list)->list:
    a=arr[:]
    for i in range(1, len(a)):
        key=a[i]
        j = i
        while j > 0 and a[j-1] > key:
            a[j] = a[j-1]
            j -= 1
        a[j]= key
    return a
def insertion_sortB(A):

    for k in range(1, len(A)): #from 1 to n-1
        current = A[k] #current element to be inserted
        j=k #find correct index for current
        while j>0 and A[j-1]>current:#element A[j-1] must be after current
            A[j]=A[j-1]
            j-=1
        A[j]=current #current el in the right place#
        
if __name__=="__main__":
    lst=[4,1,4,5,2,9]
    insertion_sort(lst)
    print(lst)
if __name__ == '__main__':
    unsorted =[random.randint(1,100) for _ in range(10)]
    print(unsorted)
    sorted=insertion_sort(unsorted)
    print(unsorted,sorted)