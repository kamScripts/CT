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

        
if __name__=="__main__":
    lst=[4,1,4,5,2,9]
    insertion_sort(lst)
    print(lst)
if __name__ == '__main__':
    unsorted =[random.randint(1,100) for _ in range(10)]
    print(unsorted)
    sorted=insertion_sort(unsorted)
    print(unsorted,sorted)