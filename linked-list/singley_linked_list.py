import unittest


class Node():

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList():
    """
    LinkedList
    """
    def __init__(self):
        self.head = None
        self.count = 0
    
    def prepend_ll(self, val):
        """
        Insert Items to first of the linked list

        Args:
            val (numeric): pass numeric value. function will generate new node of it.
        """
        node = Node(val)
        if self.head == None:
            self.head = node
        else:        
            node.next = self.head
            self.head = node
        self.count +=1
    
    def display(self, statement=None):
        """
        DISPLAY Linked List

        Args:
            statement : Statement that you need to show after the linked list print. Defaults is set to ''/white space.
        """
        current_node = self.head
        node_list = []
        while current_node:
            node_list.append(str(current_node.value))
            current_node = current_node.next
        if statement: node_list.append(f'{statement}')
        return ' -> '.join(node_list)
    
    def __display_helper(self, node, _list=[]):
        if node is None:
            return
        _list.append(str(node.value))
        self.__display_helper(node.next, _list)
        return(_list)
    
    def display_iter(self, statement=''):
        """
        DISPLAY Linked List RECURSIVE
        """
        res = self.__display_helper(self.head)
        if statement:
            res.append(statement)
        return ' -> '.join(res)

    
    def append_ll(self, value):
        """
        Insert Node to the last of the linked list
        Args:
            value (numeric): Node to add
        """
        node = Node(value)
        if self.head == None: return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            self.count +=1
        current_node.next = node
    
    def insert_at(self, index_point, value):
        """
        Insert Node at a certain Index number
        Args:
            index_point (Numeric): Nodex index
            value (Node Value):
        """
        node = Node(value)
        if not self.head: return
        if index_point == 0:
            node.next = self.head
            self.head = node
            return
        idx = 0
        current_node = self.head
        while current_node:
            if index_point - 1 == idx:
                node.next = current_node.next
                current_node.next = node
                self.count +=1
            current_node = current_node.next
            idx += 1
    
    def insert_after(self, old_node, new_val):
        """
        Insert Node After
        Args:
            old_node (Node Value):
            new_val (Node Value):
        """
        new_node = Node(new_val)
        if not self.head: return

        current_node = self.head
        while current_node:
            if current_node.value == old_node:
                new_node.next = current_node.next
                current_node.next = new_node
                self.count += 1
            current_node = current_node.next
    
    def next_node(self, node_value) -> Node:
        """
        Given Node's Next Node
        Args:
            node_value (Node Value):

        Returns:
            Node: 
        """
        current_node = self.head
        while current_node.next:
            if current_node.next.value == node_value:
                return current_node.next.next
            current_node = current_node.next
        return None

    def previous_node(self, node_value) -> Node:
        """
        Get Previous node of a given node value
        Args:
            node_value (Node Value):s
        Returns:
            Node:s
        """
        current_node = self.head
        while current_node.next:
            if current_node.next.value == node_value:
                return current_node
            current_node = current_node.next
        return None

    def insert_before(self, target_node, new_val):
        """
        Insert Before a node
        Args:
            target_node (_type_):s
            new_val (_type_):s
        """
        if not self.head: return
        new_node = Node(new_val)
        prev_node = self.previous_node(target_node)
        if prev_node:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.count +=1

    def delete_by_val(self, node_to_delete):
        """
        Delete Node by value
        Args:
            node_to_delete (_type_):s
        """
        if not self.head: return
        if self.head.value == node_to_delete:
            self.head = self.head.next
            self.count -= 1
            return
        prev_node = self.previous_node(node_to_delete)
        next_node = self.next_node(node_to_delete)
        if prev_node:
            prev_node.next = next_node
            self.count -= 1

    def delete_by_index(self, node_index):
        """
        DELETE Node by Index

        Args:
            node_index (_type_):
        """
        if not self.head: return
        if node_index == 0:
            self.head = self.head.next
            self.count -= 1
            return
        idx = 0
        current_node = self.head
        while current_node.next:
            if idx+1 == node_index:
                current_node.next = current_node.next.next
                self.count -= 1
            idx += 1
            current_node = current_node.next

    def search_element_by_value(self, node_value):
        """
        Search Node by Index

        Args:
            node_index (_type_):
        """
        if not self.head: return

        if node_value == self.head.value:
            return 0

        idx = 0
        current_node = self.head
        while current_node.next:
            if current_node.value == node_value:
                return idx
            idx += 1
            current_node = current_node.next

        if current_node.value == node_value:
            return idx
        
        return -1

    def search_element_index(self, node_index):
        """
        Search Node by Index

        Args:
            node_index (_type_):
        """
        if not self.head: return
        if node_index == 0:
            return self.head.value
        idx = 0
        current_node = self.head
        while current_node.next:
            if idx == node_index:
                return current_node.value
            idx += 1
            current_node = current_node.next
        return -1

    def delete_list(self):
        self.head = None
    
    def list_length(self):
        if not self.head: return 0
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count

class TestSingleyLL(unittest.TestCase):

    def setUp(self) -> None:
        self.ll = LinkedList()
        self.ll.prepend_ll(3)
        self.ll.prepend_ll(4)
        return super().setUp()
    
    def test_display_func(self):
        self.assertEqual(self.ll.display(), '4 -> 3')

    def test_display_iter_func(self):
        self.assertEqual(self.ll.display_iter(), '4 -> 3')

    def test_list_insert_first(self):
        self.ll.prepend_ll(6)
        self.assertEqual(self.ll.display(), '6 -> 4 -> 3')

    def test_list_insert_last(self):
        self.ll.append_ll(55)
        self.ll.append_ll(66)
        self.assertEqual(self.ll.display(), '4 -> 3 -> 55 -> 66')

    def test_list_insert_after(self):
        self.ll.insert_after(3, 27)
        self.assertEqual(self.ll.display(), '4 -> 3 -> 27')

    def test_list_insert_at(self):
        self.ll.insert_at(1, 27)
        print(self.ll.display())
        self.assertEqual(self.ll.display(), '4 -> 27 -> 3')

        
if __name__=="__main__":
    unittest.main()

    # ll.display('INSERT FIRST')

    # ll.insert_last(44)
    # ll.insert_first(88)
    # # ll.display('INSERT LAST 44')

    # ll.insert_at(2, 99)
    # # ll.display('INSERT AT 2nd pos')

    # ll.insert_after(old_node=99,new_val=77)
    # # ll.display('INSERT AFTER 99')

    # ll.insert_before(4, 2)
    # # ll.display('INSERT BEFORE 4')

    # ll.delete_by_val(88)
    # # ll.display('DELETE BY VAL 88')

    # ll.delete_by_val(44)
    # # ll.display('DELETE BY VAL 44')

    # ll.delete_by_index(0)
    # # ll.display('DELETE BY INDEX 0')

    # # ll.display()
    # ll.display_iter("RECURSIVE")

    # node = ll.search_element_by_value(77)
    # print(node)

    # node = ll.search_element_index(2)
    # print(node)

    # lenght = ll.list_length()
    # # ll.display(f'List Lenght {lenght}')

    # # node = ll.delete_list()
    # # ll.display()
