class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.next:Node=None
        
    def __repr__(self) -> str:
        return f"Node({self.data!r})" # !r modifier use __repr__ instead __str__
        
class Linked_List:
    
    def __init__(self):
        self.head = None
        
    def __str__(self) -> str:
        current =self.head
        s=""
        while current:
            s+=f'{current.data} -> '
            current = current.next
        s+="None"
        return s
    def __repr__(self) -> str:
        values=[]
        current=self.head
        while current:
            values.append(repr(current.data))
            current=current.next
        return f"LinkedList([{', '.join(values)}])"
            
    
    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next=new_node
    def copy(self):
        copied_list = Linked_List()
        current = self.head
        while current:
            copied_list.append(current.data)
            current = current.next
        return copied_list


if __name__ == "__main__":
    ll=Linked_List()
    for i in range(1,10):
        ll.append(i)
    print(ll)
    print(repr(ll))
