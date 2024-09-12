class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True   


#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
def find_kth_from_end(my_linked_list, k): 
    
    slow_ptr = my_linked_list.head 
    fast_ptr = slow_ptr 
    
    for i in range(k): 
        fast_ptr = fast_ptr.next 
        
        if fast_ptr == None and i<k-1: 
            return None
            
    while fast_ptr is not None: 
        slow_ptr = slow_ptr.next 
        fast_ptr = fast_ptr.next 
        
    return slow_ptr 

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 5
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
