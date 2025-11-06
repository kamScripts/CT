class Empty(Exception):
    """Empty deque exception"""
class Arraydeque:
    """ Deque Abstract Data Type (ADT)."""
    DEFAULT_CAPACITY=10 #moderate capacity for all new queues
    def __init__(self, max_len=None)->None:
        self.max_len = max_len
        self._data=[None]*Arraydeque.DEFAULT_CAPACITY
        self._size=0
        self._front=0

    def __len__(self):
        """Return length of the deque."""
        return self._size

    def __str__(self):
        result = []
        for i in range(self._size):
            index = (self._front + i) % len(self._data)
            result.append(str(self._data[index]))
        return ' <- '.join(result)

    def __repr__(self):
        result = []
        for i in range(self._size):
            index = (self._front + i) % len(self._data)
            result.append(str(self._data[index]))
        return ','.join(result)

    def add_first(self,e)->None:
        """Add element to the front of deque,
        if max_len set, last element is pushed out when reach
        capacity limit."""
        # if reach max len remove pop out element from the other end
        if self.max_len and self._size == self.max_len:
            self.delete_last()
            self._front = (self._front - 1) % len(self._data)
            self._data[self._front] = e
            self._size+=1
        else:
            if self._size == len(self._data):
                self._resize(2 * len(self._data))
            self._front = (self._front - 1) % len(self._data)
            self._data[self._front] = e
            self._size+=1

    def add_last(self,e)->None:
        """Add element e to the back of a deque,
        if max_len is on element at the front of deque is pushed out
        when reach capacity limit"""
        if self.max_len and self._size == self.max_len:
            self.delete_first()
            avail=(self._front+self._size)%len(self._data)
            self._data[avail]=e
            self._size+=1
        else:
            if self._size==len(self._data):
                self._resize(2*len(self._data))
            avail=(self._front+self._size)%len(self._data)
            self._data[avail]=e
            self._size+=1

    def delete_first(self):
        """Remove and return first element from deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        if 0 < self._size < len(self._data) // 4:        #Shrink array if items falls bellow 1/4 capacity
            self._resize(len(self._data) // 2)
        answer=self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size-=1
        return answer

    def delete_last(self):
        """Remove and return last element from deque"""
        if self.is_empty():
            raise Empty('Deque is empty')
        if 0 < self._size < len(self._data) // 4:        #Shrink array if items falls bellow 1/4 capacity
            self._resize(len(self._data) // 2)
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
    d=Arraydeque(10)
    #d.add_last(5)
    #d.add_first(3)
    #d.add_first(7)
    #print(d)
    #print('first',d.first(), sep=' -> ')
    #print('delete last', d.delete_last(), sep=' -> ')
    #print('len(d)', len(d), sep=' -> ')
    #print('delete last', d.delete_last(), sep=' -> ')
    #print('delete last', d.delete_last(), sep=' -> ')
    #d.add_first(6)
    #print('last', d.last(), sep=' -> ')
    #d.add_first(8)
    #d.add_first(1)
    #d.add_first(62)
    #print(d.is_empty())
    #print('last', d.last(), sep=' -> ')
    #print(d)
    #print('delete first', d.delete_first(), sep=' -> ')
    #d.add_last(89)
    #print(d)
    for num in range(14):
        d.add_first(num)
    print(d)
    for num in range(40,45):
        d.add_last(num)
    print(d)
