class Empty(Exception):
    """Empty Queue Exception"""
class LinkedQueue:
    """
    Example from Goodrich et al. Data Structures & Algorithms(2013)
    FIFO que implementation using a singly linked list for storage.
    """

    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next' #streamline memory usage

        def __init__(self, element, next) -> None:
            self._element = element     #reference to the head node
            self._next = next           #reference to the next node
        

    def __init__(self):
        """Create an empty queue."""
        self._head: 'LinkedQueue._Node | None' = None
        self._tail: 'LinkedQueue._Node | None' = None
        self._size: int = 0  #Number of queue elements

    def __len__(self):
        """Returns the number of elements in a queue."""
        return self._size

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    def enqueue(self, e):
        """Add an element to the bac of the queue."""
        newest = self._Node(e, None)   #node will be new tail
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
if __name__ == '__main__':
    Q = LinkedQueue()
    for i in range(20):
        Q.enqueue(i)
    for i in range(20):
        print(Q.dequeue())
    print(Q.is_empty())