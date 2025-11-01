import os

def disk_usage(path:str)->int:
    """
    Example from Goodrich et al.(2013) ,
    Data Structures & Algorithms, J.Wiley & Sons, Inc.
    An Algo for computing the cumulative disk space usage nested at
    a file system entry
    
    path: valid file-system path
    
    returns: (int) cumulative path size in bytes.
    """
    total=os.path.getsize(path) #account for direct usage/ getsize() -> immediate disk usage
    if os.path.isdir(path):                                # check if is directory
        for filename in os.listdir(path):                  # for each child
            childpath=os.path.join(path, filename)         #compose a full path to a child
            total+=disk_usage(childpath)                   # add child's usage to total
    print(f'{total:<7} {path}')
    return total
disk_usage('C:\\netbeans')
            