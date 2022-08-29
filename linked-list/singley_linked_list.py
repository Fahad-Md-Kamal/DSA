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
    
    def insert_first(self, val):
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
    
    def display(self, statement=''):
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
        node_list.append(f'{statement}')
        print(' -> '.join(node_list))
    
    def insert_last(self, value):
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
        idx = 0
        current_node = self.head
        while current_node.next:
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
        while current_node.next:
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

        
if __name__=="__main__":
    ll = LinkedList()
    ll.insert_first(3)
    ll.insert_first(4)
    ll.insert_first(5)
    ll.insert_first(6)
    ll.display('INSERT FIRST')

    ll.insert_last(44)
    ll.insert_first(88)
    ll.display('INSERT LAST 44')

    ll.insert_at(2, 99)
    ll.display('INSERT AT 2nd pos')

    ll.insert_after(old_node=99,new_val=77)
    ll.display('INSERT AFTER 99')

    ll.insert_before(4, 2)
    ll.display('INSERT BEFORE 4')

    ll.delete_by_val(88)
    ll.display('DELETE BY VAL 88')

    ll.delete_by_val(44)
    ll.display('DELETE BY VAL 44')

    ll.delete_by_index(0)
    ll.display('DELETE BY INDEX 0')
