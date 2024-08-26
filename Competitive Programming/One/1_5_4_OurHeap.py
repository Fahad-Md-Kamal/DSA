class OurHeap:

    def __init__(self, items) -> None:
        self.heap = [None]
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, x):
        if x not in self.rank:
            i = len(self.heap)
            self.heap.append(x)  # add new leaf
            self.rank[x] = i
            self.up(i)  # maintain heap order

    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()  # remove last leaf
        if self:  # if heap is not empty
            self.heap[1] = x  # move the last leaf
            self.rank[x] = 1  # to the root
            self.down(1)  # maintain heap order
        return root

    def up(self, i):
        x = self.heap[i]
        while i > 1 and x < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2
        self.heap[i] = x  # insertion index found
        self.rank[x] = i

    def down(self, i):
        x = self.heap[i]
        n = len(self.heap)

        while True:
            left = 2 * i
            right = left + 1
            print(self.heap[right])
            print(self.heap[left])

            if (right < n and self.heap[right] < x and self.heap[right] < self.heap[left]):
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i  # move right child up
                print("."*30)

            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i
                i = left
                print("")

            else:
                self.heap[i] = x  # insertion index found
                self.rank[x] = i
                print("")
                return

    def update(self, old, new):
        i = self.rank[old]  # change value at index i
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:  # maintain heap order
            self.down(i)
        else:
            self.up(i)


if __name__ == "__main__":
    heap = OurHeap([7, 8, 9, 11, 12, 1, 2, 4, 5, 6])
    print("HEAP:\t", heap.heap)
    print("RANK:\t", heap.rank)

    heap.push(1)
    heap.push(1)
    print("HEAP:\t", heap.heap)
    print("RANK:\t", heap.rank)

    heap.pop()
    print("HEAP:\t", heap.heap)
    print("RANK:\t", heap.rank)
