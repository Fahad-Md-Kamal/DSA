
from locale import currency


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data


class LinkedList():

    def __init__(self):
        self.head : Node = None

    def ll_print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    
    def print_node_from(self, node):
        start_node = None
        head_node = self.head
        while self.head.next != head_node:
            if self.head.data == node:
                start_node = self.head
                break
            self.head = self.head.next
        
        if not start_node:
            raise Exception

        llstr = []
        head_node = start_node
        while True:
            llstr.append(str(start_node.data))
            if start_node.next == head_node:
                break
            start_node = start_node.next
        print(" --> ".join(llstr))

    def total_items(self):
        count = 0
        if not self.head: 
            count = 0
        else:
            current = self.head
            while current:
                count += 1
                print(current.next.data, end=' --> ')
                current = self.head.next
        print(count)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def insert_list_values(self, data:list):
        # self.head = None
        for i in data:
            self.insert_at_end(i)

    def add_list_values(self, data:list):
        for i in data:
            self.insert_at_end(i)
    
    def insert_at_start(self, data):
        prev_current = self.head
        self.head = Node(data)
        self.head.next = prev_current
    
    def insert_at_index(self, index, data):
        if not self.head:
            self.head = Node(data)
            return

        idx = 0
        current = self.head
        while current.next:
            if idx == index-1:
                old_node = current.next
                new_node = Node(data)
                new_node.next = old_node
                current.next = new_node
                break
            current = current.next
            idx += 1
    
    def insert_after_value(self, value, data):
        if not self.head:
            raise Exception("List empty")

        current = self.head
        while current.next:
            if current.data == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception(f"List does not contains {value}")
    
    def insert_before_value(self, value, data):
        if not self.head:
            raise Exception("List empty")

        current = self.head
        while current.next:
            if current.next.data == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception(f"List does not contains {value}")

    # Reverse the list
    def reverse_list(self):
        if not self.head:
            raise Exception("List is Empty")
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
    
    def convert_to_circular(self):
        if not self.head:
            raise Exception("Head is empty")
        
        head_node = self.head

        current = self.head

        while current.next != head_node:
            if not current.next:
                current.next = head_node
            else:
                current = current.next

    # Make it circular list
    # Count total item of the list
    # list total dynamic sum


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_list_values(["banana","mango","grapes","orange"])
    ll.add_list_values(["dates","penuts","watermelon","jackfruit"])
    ll.insert_at_start('calander')
    ll.insert_at_index(1, 'tada')
    ll.insert_after_value('penuts', 'guava')
    ll.insert_before_value('mango', 'strawbery')
    ll.ll_print()
    ll.total_items()
    ll.reverse_list()
    ll.ll_print()
    ll.convert_to_circular()
    ll.print_node_from('dates')











    
    # def insert_node_at_end(self, data):

    #     if self.head is None:
    #         self.head = Node(data)
    #         return

    #     _current = self.head

    #     while _current.next:
    #         _current = _current.next
            
    #     _current.next=Node(data=data)
    
    # def insert_list_values(self, list_values: list):
    #     for n in list_values:
    #         self.insert_node(n)
            

# """

#     ############## Singly Linked List  ##############

#     # 1. Introduction to Linked List
#     # 2. Linked List vs Array
#     3. Linked List Insertion
#     4. Linked List Deletion (Deleting a given key)
#     5. Linked List Deletion (Deleting a key at given position)
#     6. Write a function to delete a Linked List
#     7. Find Length of a Linked List (Iterative and Recursive)
#     8. Search an element in a Linked List (Iterative and Recursive)
#     9. Write a function to get Nth node in a Linked List
#     10. Nth node from the end of a Linked List
#     11. Print the middle of a given linked list
#     12. Write a function that counts the number of times a given int occurs in a Linked List
#     13. Detect loop in a linked list
#     14. Find length of loop in linked list
#     15. Function to check if a singly linked list is palindrome
#     16. Remove duplicates from a sorted linked list
#     17. Remove duplicates from an unsorted linked list
#     18. Swap nodes in a linked list without swapping data
#     19. Pairwise swap elements of a given linked list
#     20. Move last element to front of a given Linked List
#     21. Intersection of two Sorted Linked Lists
#     22. Intersection point of two Linked Lists.
#     23. QuickSort on Singly Linked List
#     24. Segregate even and odd nodes in a Linked List
#     25. Reverse a linked list


#     ############ Circular Link List ######################

#     1. Circular Linked List Introduction and Applications
#     2. Circular Linked List Traversal
#     3. Split a Circular Linked List into two halves
#     4. Sorted insert for circular linked list
#     5. Check if a linked list is Circular Linked List
#     6. Convert a Binary Tree to a Circular Doubly Link List
#     7. Circular Singly Linked List | Insertion
#     8. Deletion from a Circular Linked List
#     9. Circular Queue | Set 2 (Circular Linked List Implementation)
#     10. Count nodes in Circular linked list
#     11. Josephus Circle using circular linked list
#     12. Convert singly linked list into circular linked list
#     13. Circular Linked List | Set 1 (Introduction and Applications)
#     14. Circular Linked List | Set 2 (Traversal)
#     15. Implementation of Deque using circular array
#     16. Exchange first and last nodes in Circular Linked List


#     ################ Doubly Linked List  ######################

#    1. Doubly Linked List Introduction and Insertion
#    2. Delete a node in a Doubly Linked List
#    3. Reverse a Doubly Linked List
#    4. The Great Tree-List Recursion Problem.
#    5. Copy a linked list with next and arbit pointer
#    6. QuickSort on Doubly Linked List
#    7. Swap Kth node from beginning with Kth node from end in a Linked List
#    8. Merge Sort for Doubly Linked List
#    9. Create a Doubly Linked List from a Ternary Tree
#    10. Find pairs with given sum in doubly linked list
#    11. Insert value in sorted way in a sorted doubly linked list
#    12. Delete a Doubly Linked List node at a given position
#    13. Count triplets in a sorted doubly linked list whose sum is equal to a given value x
#    14. Remove duplicates from a sorted doubly linked list
#    15. Delete all occurrences of a given key in a doubly linked list
#    16. Remove duplicates from an unsorted doubly linked list
#    17. Sort the biotonic doubly linked list
#    18. Sort a k sorted doubly linked list
#    19. Convert a given Binary Tree to Doubly Linked List | Set
#    20. Program to find size of Doubly Linked List
#    21. Sorted insert in a doubly linked list with head and tail pointers
#    22. Large number arithmetic using doubly linked list
#    23. Rotate Doubly linked list by N nodes
#    24. Priority Queue using doubly linked list
#    25. Reverse a doubly linked list in groups of given size
#    26. Doubly Circular Linked List | Set 1 (Introduction and Insertion)
#    27. Doubly Circular Linked List | Set 2 (Deletion)


#     ################### Misc  ######################

#    1. Skip List | Set 1 (Introduction)
#    2. Skip List | Set 2 (Insertion)
#    3. Skip List | Set 3 (Searching and Deletion)
#    4. Reverse a stack without using extra space in O(n)
#    5. An interesting method to print reverse of a linked list
#    6. Linked List representation of Disjoint Set Data Structures
#    7. Sublist Search (Search a linked list in another list)
#    8. How to insert elements in C++ STL List ?
#    9. Unrolled Linked List | Set 1 (Introduction)
#    10. A Programmer’s approach of looking at Array vs. Linked List
#    11. How to write C functions that modify head pointer of a Linked List?
#    12. Given a linked list which is sorted, how will you insert in sorted way
#    13. Can we reverse a linked list in less than O(n)?
#    14. Practice questions for Linked List and Recursion
#    15. Construct a Maximum Sum Linked List out of two Sorted Linked Lists having some Common nodes
#    16. Given only a pointer to a node to be deleted in a singly linked list, how do you delete it?
#    17. Why Quick Sort preferred for Arrays and Merge Sort for Linked Lists?
#    18. Squareroot(n)-th node in a Linked List
#    19. Find the fractional (or n/k – th) node in linked list
#    20. Find modular node in a linked list
#    21. Construct a linked list from 2D matrix
#    22. Find smallest and largest elements in singly linked list
#    23. Arrange consonants and vowels nodes in a linked list
#    24. Partitioning a linked list around a given value and If we don’t care about making the elements of the list “stable”
#    25. Modify contents of Linked List

# """