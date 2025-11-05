class Stack:
    def __init__(self,items=None) -> None:
        self.items = [] if items is None else items

    def __str__(self):
            return f"Stack(top → bottom): {list(reversed(self.items))}"

    def __repr__(self):
        return self.items


    def push(self,value):
        self.items.append(value)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items)==0
    
if __name__=="__main__":
    stack=Stack()
    stack1=Stack()
    
    stack.push(10)
    stack.push(20)
    stack.push(stack1)
    
    stack1.push(11)
    stack1.push(22)
    stack1.push(33)
    
    print(stack)