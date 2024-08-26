

class OurQueue:

    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)
    
    def push(self, obj):
        self.in_stack.append(obj)
    
    def pop(self):
        if not self.out_stack:
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()
    
    def print_stock(self):
        print("In Stack:\t", self.in_stack)
        print("Out Stack:\t", self.out_stack)
    

if __name__ == "__main__":
    queue = OurQueue()
    queue.push(1)
    queue.push(11)
    queue.push(13)
    queue.push(14)
    queue.push(71)

    queue.print_stock()

    queue.pop()
    queue.print_stock()
