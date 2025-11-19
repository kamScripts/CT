def reverse_string(s:str)-> str:
    """Reverse a string recursively."""
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

def recursive_palindrome(s:str)->bool:
    """Return True if string is palindrome."""
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive_palindrome(s[1:-1])


if __name__=='__main__':

    #print(reverse_string('software development'))
    print(recursive_palindrome('racecar'))