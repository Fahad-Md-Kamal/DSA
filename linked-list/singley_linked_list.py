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
    
    def append_list_from_array(self, data_list):
        if not isinstance(data_list, list): return
        for data in data_list:
            self.append(data)
        
    # Previous Node by index
    def previous_index_node(self, index):
        if not self.head: return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                return current
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
                return current_node.next
            current_node = current_node.next
            count +=1
        return None

    # Previous Node by val
    def previous_node_of_val(self, data):
        if not self.head: return
        current_node = self.head
        while current_node and current_node.next:
            if current_node.next.data == data:
                return current_node.data
            current_node = current_node.next
        return None

    # Next Node by val
    def next_node_of_val(self, data):
        if not self.head: return
        current_node = self.head
        while current_node and current_node.next:
            if current_node.data == data:
                return current_node.next.data
            current_node = current_node.next
        return

    # Insert at index
    def insert_at_index(self, index, data):
        if not self.head: return
        new_node = Node(data)

        prev_node = self.previous_index_node(index)
        if prev_node: 
            new_node.next = prev_node.next
            prev_node.next = new_node

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
    
    def test_append_list_from_data_list(self):
        self.ll.append_list_from_array([1,2,3,4])
        self.assertEqual(self.ll.display(), '1 -> 2 -> 3 -> 4')
    
    def test_create_list_from_data_empty_list(self):
        self.ll.append_list_from_array([])
        self.assertEqual(self.ll.display(), [])
    
    def test_previous_index_node(self):
        self.ll.append_list_from_array([9,12,15])
        node = self.ll.previous_index_node(2)
        self.assertEqual(node.data, 12)
    
    def test_previous_index_node_for_first(self):
        self.ll.append_list_from_array([9, 12])
        node = self.ll.previous_index_node(1)
        self.assertEqual(node.data, 9)
    
    def test_previous_index_node_for_out_of_bound(self):
        self.ll.append_list_from_array([9, 17])
        self.assertEqual(self.ll.previous_index_node(10), None)
    
    def test_previous_index_node_for_zero_index(self):
        self.ll.append(9)
        self.assertEqual(self.ll.previous_index_node(0), None)
    
    def test_next_index_node(self):
        self.ll.append_list_from_array([9, 12, 15])
        node = self.ll.next_index_node(0)
        self.assertEqual(node.data, 12)
    
    def test_next_index_node_negative_index(self):
        self.ll.append_list_from_array([9, 12])
        node = self.ll.next_index_node(-1)
        self.assertEqual(node, None)
    
    def test_next_index_node_last_index(self):
        self.ll.append_list_from_array([9, 12])
        node = self.ll.next_index_node(-1)
        self.assertEqual(node, None)
    
    def test_previous_node_of_data(self):
        self.ll.append_list_from_array([9, 12])
        self.assertEqual(self.ll.previous_node_of_val(12), 9)

    def test_previous_node_of_data_empty(self):
        self.assertEqual(self.ll.previous_node_of_val(1), None)

    def test_previous_node_of_data_out_bound(self):
        self.ll.append(13)
        self.assertEqual(self.ll.previous_node_of_val(2), None)
    
    def test_next_node_of_val(self):
        self.ll.append_list_from_array([33, 66])
        self.assertEqual(self.ll.next_node_of_val(33), 66)
    
    def test_next_node_of_val_not_in_list(self):
        self.ll.append_list_from_array([33, 66])
        self.assertEqual(self.ll.next_node_of_val(44), None)
    
    def test_next_node_of_val_emapty_list(self):
        self.assertEqual(self.ll.next_node_of_val(44), None)
    
    def test_insert_at_index_empty_list(self):
        self.ll.append_list_from_array([])
        self.ll.insert_at_index(index=1, data=44)
        self.assertEqual(self.ll.display(), [])
    
    def test_insert_at_index(self):
        self.ll.append_list_from_array([1,2,3,4])
        self.ll.insert_at_index(index=1, data=44)
        self.assertEqual(self.ll.display(), '1 -> 44 -> 2 -> 3 -> 4')
    
    def test_insert_at_index_last_index(self):
        self.ll.append_list_from_array([1,2,3,4])
        self.ll.insert_at_index(index=5, data=44)
        self.assertEqual(self.ll.display(), '1 -> 2 -> 3 -> 4')
    

if __name__ == '__main__':
    unittest.main()