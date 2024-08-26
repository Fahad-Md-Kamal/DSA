

class MyQueue:

    def __init__(self, items):
        self.my_stake = []
        for i in items:
            self.my_stake.append(i)

    def push(self, item):
        self.my_stake.append(item)
        