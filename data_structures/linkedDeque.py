from double_linked_list import _DoublyLinkedList

class Empty(Exception):
    """Empty Queue exception"""

class LinkedDeque(_DoublyLinkedList):
    """Double-ended queue implementation based on doubly linked list."""

    def first(self):
        """Return but do not remove first element of the list."""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._header._next._element # first real item before header- sentinel
    def last(self):
        """Return (but do not remove) last elment of the list."""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._trailer._prev._element # last real element before trailer - sentinel
    def insert_first(self,e):
        """Insert element at front of the deque."""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        self._insert_between(e,self._header, self._header._next) # after header
    def insert_last(self, e):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        self._insert_between(e,self._trailer._prev, self._trailer) # before trailer
    def delete_first(self):
        """Delete first element of deque."""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._delete_node(self._header._next)
    def delete_last(self):
        """Delete last element of a deque."""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._delete_node(self._trailer._prev)
