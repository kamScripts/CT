class Empty(Exception):
    """Exception attempting to access an element from an empty container."""
class Full(Exception):
    """Exception attempting to push into full stack."""
class ArrayStack:
    """Example from Goodrich et al. Data Structures & Algorithms(2013)
    LIFO Stack implementation using a Python list as underlying storage
    """
    def __init__(self,data=None, max_len=None):
        """Create an empty stack."""
        self._data=[] if data is None else data
        self._size=0
        self._max_len=max_len
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def __str__(self):
        
        prnt = [str(item) for item in self._data]
        prnt.reverse()
        return f"Stack top -> bottom: \n\t{'\n\t'.join(prnt)}"
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data)==0
    def push(self,e):
        """Add element e to the top of the stack."""
        if self._max_len and len(self._data)==self._max_len:
            raise Full('The stack raised maximum capacity')
        self._data.append(e)    #New item stored at the end of the list
    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        """
        Remove and return the element from the top of the stack (LIFO).
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    def transfer(self,s,t):
        """Transfer Stack S into  empty T where S,last=t.top"""
        for _ in range(len(s)):
            t.push(s.pop())
    def clear(self):
        """Removes all elements from a stack"""
        if not self._data:
            return
        self.pop()
        self.clear()
if __name__=='__main__':
    l=[1,2,3,4,5,6,7,8,9,10]
    S=ArrayStack()
    
    for num in l:
        S.push(num)
    print(S)
    print('S top:',S.top())
    T=ArrayStack()
    T.transfer(S,T)
    T.clear()
    print(T)
    T.top()
