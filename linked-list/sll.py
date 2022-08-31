import unittest


# Create Node
class Node:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next = next_node

# Create Linked List
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    # Display Iterative
    def display(self):
        if not self.head: return []
        data_list = []
        current_node = self.head
        while current_node:
            data_list.append(str(current_node.data))
            current_node = current_node.next
        return ' -> '.join(data_list)
    
    # Helper for recursive Process
    def _display_helper(self, node, data_list=[]) -> list:
        if not node: return
        data_list.append(str(node.data))
        self._display_helper(node.next, data_list)
        return data_list
            
    # Display Reverse
    def display_recur(self):
        if not self.head: return []
        data_list = self._display_helper(self.head)
        return ' -> '.join(data_list)
        
    # Append / Insert at End
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        self.tail = node
        self.count += 1

    # Prepend / Insert at Begining
    def prepend(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
            self.count += 1
            return
        node.next = self.head
        self.head = node
        self.count += 1
        
    # Previous Node by index
    def previous_index_node(self, index):
        if not self.head: return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                return current.data
            current = current.next
            count += 1
        return None

    # After Node by index
    def next_index_node(self, index):
        if not self.head: return
        count = 0
        current_node = self.head
        while current_node and current_node.next:
            if count == index:
                return current_node.next.data
            current_node = current_node.next
            count +=1
        return None

# Previous Node by val
# After Node by val

# Insert at index
# Insert before index
# Insert After index

# Insert before value
# Insert After value

# Remove at index
# Remove before index
# Remove after index

# Remove before value
# Remove after value

class TestSingleyLL(unittest.TestCase):

    def setUp(self) -> None:
        self.ll = LinkedList()
        return super().setUp()
    
    def test_display_with_empty(self):
        self.assertEqual(self.ll.display(), [])
    
    def test_display_rec_with_empty(self):
        self.assertEqual(self.ll.display_recur(), [])
    
    def test_append(self):
        self.ll.append(9)
        self.ll.append(12)
        self.assertEqual(self.ll.display(), '9 -> 12')
    
    def test_prepend(self):
        self.ll.prepend(5)
        self.ll.prepend(2)
        self.assertEqual(self.ll.display(), '2 -> 5')
    
    def test_prepend_with_single_value(self):
        self.ll.prepend(33)
        self.assertEqual(self.ll.display(), '33')
    
    def test_previous_index_node(self):
        self.ll.append(9)
        self.ll.append(12)
        self.ll.append(15)
        self.assertEqual(self.ll.previous_index_node(2), 12)
    
    def test_previous_index_node_for_first(self):
        self.ll.append(9)
        self.ll.append(12)
        self.assertEqual(self.ll.previous_index_node(1), 9)
    
    def test_previous_index_node_for_out_of_bound(self):
        self.ll.append(9)
        self.ll.append(17)
        self.assertEqual(self.ll.previous_index_node(10), None)
    
    def test_previous_index_node_for_zero_index(self):
        self.ll.append(9)
        self.assertEqual(self.ll.previous_index_node(0), None)
    
    def test_next_index_node(self):
        self.ll.append(9)
        self.ll.append(12)
        self.ll.append(15)
        self.assertEqual(self.ll.next_index_node(0), 12)
    
    def test_next_index_node_negative_index(self):
        self.ll.append(9)
        self.ll.append(12)
        self.assertEqual(self.ll.next_index_node(-1), None)
    
    def test_next_index_node_last_index(self):
        self.ll.append(9)
        self.ll.append(12)
        self.assertEqual(self.ll.next_index_node(1), None)


if __name__ == '__main__':
    unittest.main()
    # ll = LinkedList()
    # ll.append(9)
    # ll.append(12)
    # print(ll.previous_index_node(0))
    # print(ll.display_recur())