# https://www.youtube.com/playlist?list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_data(self, prev_node, data):
        new_node = Node(data)

        if not prev_node:
            print("Previous node is not in the list")
            return
        
        last_node = self.head
        while last_node.next:
            if last_node.data == prev_node:
                new_node.next = last_node.next
                last_node.next = new_node
                return
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

if __name__ == '__main__':
    llist = LinkedList()

    llist.append('B')
    llist.append('C')
    llist.append('D')
    # llist.print_list()

    llist.prepend('A')
    # llist.print_list()
    llist.insert_after_data('A', 'K')
    # llist.print_list()
    llist.insert_after_node(llist.head.next, 'Z')
    llist.print_list()
