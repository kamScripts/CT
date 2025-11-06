class Empty(Exception):
    """Exception attempting to access an element from an empty container."""
class Full(Exception):
    """Exception attempting to push into full stack."""
class ArrayStack:
    """Example from Goodrich et al. Data Structures & Algorithms(2013)
    LIFO Stack implementation using a Python list as underlying storage
    """

    def __init__(self):
        """Create an empty stack."""
        self._data=[]
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data)==0
    def push(self,e):
        """Add element e to the top of the stack."""
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
        for _ in range(len(S)):
            t.push(s.pop())
        
l=[1,2,3,4,5]
S=ArrayStack()

for num in l:
    S.push(num)
print(S.top(),S._data, sep=('-> '))
T=ArrayStack()
T.transfer(S,T)
print(T.top(),T._data,sep='-> ')