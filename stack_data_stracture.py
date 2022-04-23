class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def get_stack(self):
        return self.items
    
if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push('A')
    s.push('B')
    s.push('D')
    s.push('C')
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
    print(s.peek())
