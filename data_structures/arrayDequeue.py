class Empty(Exception):
    """Empty deque exception"""
class Arraydeque:
    """The Deque Abstract Data Type (ADT)"""
    DEFAULT_CAPACITY=10 #moderate capacity for all new queues
    def __init__(self)->None:
        self._data=[None]*Arraydeque.DEFAULT_CAPACITY
        self._size=0
        self._front=0
        
    def __len__(self):
        """Return length of the deque."""
        return self._size
    def add_first(self,e)->None:
        answer=self._data[self._front]
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size+=1
        
        return answer
    def add_last(self,e)->None:
        """Add element e to the back of a deque."""
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1
        
    def delete_first(self):
        """Remove and return first element from deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        answer=self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front - 1) % len(self._data)
        self._size-=1
        return answer
        
    def delete_last(self):
        """Remove and return last element from deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[(self._front+self._size-1) % len(self._data)]
        self._data[(self._front+self._size-1) % len(self._data)] = None
        self._size -= 1
        return answer
        
    def first(self):
        """Return(but do not remove) the first el of deque
        raise exception if is empty."""
        if self.is_empty():
            raise Empty("deque is empty")
        return self._data[self._front]
    def last(self):
        """Return  (but do not remove) the last element of deque;
        error occurs if deque is empty"""
        if self.is_empty():
            raise Empty('deque is empty')
        return self._data[(self._front+self._size-1) % len(self._data)]
    def is_empty(self):
        """Return True if deque is empty."""
        return self._size==0
    def _resize(self, cap:int)->None:
        """Resize a deque if reach max capacity"""
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1 + walk) % len(old)
        self._front = 0
if __name__=="__main__":
    
    d=Arraydeque()
    d.add_last(5)
    d.add_first(3)
    d.add_first(7)
    print('deque:',d._data,sep=' -> ')
    print('first',d.first(), sep=' -> ')
    print('delete last', d.delete_last(), sep=' -> ')
    print('len(d)', len(d), sep=' -> ')
    print('delete last', d.delete_last(), sep=' -> ')
    print('delete last', d.delete_last(), sep=' -> ')
    d.add_first(6)
    print('last', d.last(), sep=' -> ')
    d.add_first(8)
    print(d.is_empty())
    print('last', d.last(), sep=' -> ')
