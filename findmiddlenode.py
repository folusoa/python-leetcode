#find middle node

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
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):

        #edge cases

        #empty list 
        if self.head == None:
            return None
        
        #single node
        if self.head == self.tail:
            return self.head
        
        else: 
            slow_ptr = self.head 
            fast_ptr = slow_ptr

            while fast_ptr.next:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next 
                
                #break out of the while loop if ptr is none
                if not fast_ptr: 
                    break

            return slow_ptr



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
#my_linked_list.append(8)


print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""