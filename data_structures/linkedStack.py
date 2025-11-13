class Empty(Exception):
    """Empty Exception"""
class LinkedStack:
    """
    Example from Goodrich et al. Data Structures & Algorithms(2013)
    LIFO Stack implementation using a singly linked linked list for storage.
    """

    # -------------------> nested _Node class <-------------------
    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next' #streamline memory usage

        def __init__(self, element, next) -> None:
            self._element = element     #reference to the head node
            self._next = next           #reference to the next node
    # -------------------> stack methods <-------------------
    def __init__(self):
        """Create an empty stack"""
        self._head: 'LinkedStack._Node | None' = None
        self._size = 0                  #number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if stack is empty."""
        return self._size==0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head) #create and link a new node
        self._size += 1
    def top(self):
        """Return (but do not remove) the element at the of the stack
        Raise Empty Exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._head._element              #top of stack is at head of list
    def pop(self):
        """Remove and return the element from the top of the stack (LIFO)
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is Empty')
        answer = self._head._element
        self._head = self._head._next           #bypass the former to node
        self._size -= 1
        return answer
if __name__ == '__main__':
    stack = LinkedStack()
    stack.push([1,2,3,4,5])
    stack.push('abc')
    print(stack.top())
    stack.pop()
    print(stack.top())
