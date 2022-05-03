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
    
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node == None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if not current_node:
            return

        prev.next = current_node.next

    
    def delete_at_position(self, position):
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            current_node == None
            return

        prev = None
        count = 0
        while current_node and count != position:
            prev = current_node
            current_node = current_node.next
            count += 1

        if not current_node:
            return

        prev.next = current_node.next
        current_node = None
    
    def len_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            count += 1
        print(count)
    
    def len_recursive(self, node):
        if not node:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def len_recursive_alt(self, node):
        return 0 if not node else 1 + self.len_recursive(node.next)





if __name__ == '__main__':
    llist = LinkedList()

    llist.prepend('A')
    llist.append('B')
    llist.append('C')
    llist.append('D')
    llist.append('E')
    llist.append('F')
    # llist.print_list()

    # llist.print_list()
    # llist.insert_after_data('A', 'K')
    # # llist.print_list()
    # llist.insert_after_node(llist.head.next, 'Z')
    # llist.print_list()
    # llist.delete_node('B')
    # llist.delete_at_position(2)
    # llist.print_list()
    # llist.len_iterative()
    print(llist.len_recursive(llist.head))
