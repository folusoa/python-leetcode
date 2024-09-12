#reverse double linked list 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def reverse(self):

        ptr = self.head
        _ptr = ptr
        for _ in range(self.length):
            next_ptr = ptr.next  
            ptr.next = ptr.prev 
            ptr.prev = next_ptr
            ptr = ptr.prev

        
        self.head = self.tail 
        self.tail = _ptr
    
        return self.head
    
def main(): 

    my_doubly_linked_list = DoublyLinkedList("A")
    #my_doubly_linked_list.append("B")
    my_doubly_linked_list.append("C")
    #my_doubly_linked_list.append("D")


    print('DLL before reverse():')
    my_doubly_linked_list.print_list()


    my_doubly_linked_list.reverse()


    print('\nDLL after reverse():')
    my_doubly_linked_list.print_list()



    """
        EXPECTED OUTPUT:
        ----------------
        DLL before swap_first_last():
        1
        2
        3
        4

        DLL after swap_first_last():
        4
        2
        3
        1

    """

if __name__ == "__main__":
    main()