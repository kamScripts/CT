"""
    Examples from Goodrich et al.(2013) , Data Structures & Algorithms, J.Wiley & Sons, Inc.    
"""

def merge(S1, S2,S):
    """Merge two sorted lists S1 and S2 into properly sized list S."""
    i=j=0
    while i + j <len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]  #copy i-th element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1          #copy j-th element of S2 as next item of S

def merge_sort(S):
    """Sort the elements of list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return  #list is already sorted
    #divide
    mid = n // 2
    S1 = S[0:mid]   #copy 1st half
    S2 = S[mid:n]   #copy 2nd half
    #conquer (with recursion)
    merge_sort(S1)  #sort copy of first half
    merge_sort(S2)  #sort copy of second half
    # merge results
    merge(S1,S2,S)
    