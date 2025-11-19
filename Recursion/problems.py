def reverse_string(s:str)-> str:
    """Reverse a string recursively."""
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

if __name__=='__main__':

    print(reverse_string('software development'))