def counting_sort(arr:list[int]):
    # 1. find max value
    m = max(arr)
    # 2. Create list of length m + 1
    counts = [0] * (m+1)

    for val in arr:
    # 3 Store count of each value in corresponding index in counts[]
        counts[val]+=1
    # 4 Store cumulative sum of a counts[]
    cumulative = [0]*len(counts)
    cumulative[0]=counts[0]
    for i in range(1,len(counts)):
        cumulative[i]=counts[i]+cumulative[i-1]
    print(counts,cumulative,sep='\n')
counting_sort([6,0,0,3,4,2,1,1,6,3,3,1,2])