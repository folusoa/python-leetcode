#linked list Practice 

#the head of a linked list is a pointer or a node? 
#A node is value and pointer. two parms => value and pointer

#constructor should create a new node with value & point to null 
class Node: 
    def __init__(self, value):
        #print("did we get here? Node")
        self.value = value
        self.next = None

#should add a node to the list
#remove a node from the end of the list
class LinkedList:   

    #to be called only when creating a new Linked List 
    #assigns head to the first node created
    def __init__(self, value): 
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    #add a value to the top of the list 
    def prepend(self, value):
        newNode = Node(value)

        if self.length == 0: 
            self.head = newNode
            self.tail = newNode
            
        else:         
            newNode.next = self.head
            self.head = newNode 
        
        self.length += 1
        return newNode

    
    #add a value to the end of a Linked List
    def append(self, value): 

        newNode = Node(value)
        if self.length: 
            itr = self.tail
            itr.next = newNode
            self.tail = newNode

        else: 
            self.head = newNode
            self.tail = newNode

        self.length += 1
        return newNode


    #remove the first node
    def popFirst(self):

        #empty list
        if self.length == 0: 
            return None
        
        if self.length: 

            #single node
            if self.head == self.tail: 
                temp = self.head
                self.head = self.tail = None
                self.length -= 1
                return temp
    
            else: 
                itr = self.head
                self.head = itr.next
                itr.next = None   
                self.length -= 1
                return itr


    #get an element from the linked list by it's index 
    #returns a pointer to the node holding that value 
    def get(self, index): 
        
        #make sure it is a valid index   
        #returns none if the list is empty
        if index >= 0 and index < self.length: 

            itr = self.head
            for i in range(index):
                itr = itr.next
            return itr
         
        return None 

    #change the value of an element in a linked list given the index
    def setV(self, index, value): 

        itr = self.get(index)

        if itr: 
            itr.value = value
            #return True

        #return False

        return itr
    
    #insert a node at a particular index
    def insert(self, index, value): 

        newNode = Node(value)
        #edge case: insert at the head
        if index == 0:
            return self.prepend(value)
        
        #edge case: insert at the tail
        if index == self.length:
            return self.append(value)
        
        elif index > 0 and index < self.length: 
            
            prev = self.get(index-1)
            itr = prev.next 

            prev.next = newNode 
            newNode.next  = itr
            return newNode

        #invalid Index 
        return None

    #remove a node from the end of a LL
    #we do not care about the value or the index    
    def pop(self): 

        if self.length == 0: 
            return None
        
        elif self.head == self.tail:
            curr = self.head
            self.head = self.tail = None
            self.length -= 1
            return curr
        
        else:
            pre = curr = self.head

            while curr.next != None: 
                pre = curr
                curr = curr.next
            
            self.tail = pre 
            pre.next = None
            self.length -= 1
            
            return curr
    
    #remove a node at a particular index
    def remove(self, index): 

        #methods already have return statements
        if index == 0: 
            return self.popFirst()
            
        if index == self.length-1: 
            return self.pop()
            
        elif index > 0 and index < self.length: 
            prev = self.get(index-1)
            
            if prev.next: 
                node = prev.next
                prev.next = node.next
                node.next = None
                self.length -= 1
            
                return node
            
        return None

    #removes a node by value from a LL 
    def removeNode(self, value):

        #edge case: list is empty
        if self.length == 0: 
            return None
     
        #edge case: there is only one node
        if self.head == self.tail and self.head.value == value: 
            self.head = None
            self.tail = None
            self.length -= 1

        #edge case: the value is at the head of the LL 
        elif self.head.value == value and self.length > 1:
            self.popFirst()
              
        else:  
            pre = curr = self.head      
           
            while curr != None: 
                            
                #print("did we get here? while loop")
                if curr.value == value:   
                    if curr == self.tail: 
                        self.tail = pre
                     
                    pre.next = curr.next 
                    curr.next = None
                    curr = pre.next
                    self.length -= 1

                else:
                    pre = curr                                          
                    curr = curr.next

            if self.length == 1:
                self.tail = self.head

    def reverseList(self): 

        if self.length > 0: 

            if self.length == 1: 
                return self
            
            prev = None
            curr = self.head 
            frwd = curr.next
           
            while frwd != None:
                curr.next = prev
                prev = curr
                curr = frwd
                frwd = frwd.next
            
            curr.next = prev
            
            #swap the head and tail 
            my_temp = self.head
            self.head = self.tail 
            self.tail = my_temp  
            
            return self

        return None


    def printLL(self): 
        if self.length == 0:
            print("The list is empty")

        #goal is to have a pointer that inherits the same abilities as the head pointer. 
        iter = self.head
        while iter != None: 
            print (iter.value)
            iter = iter.next 

    
def main(): 
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
   
    my_linked_list.printLL()

    my_linked_list.reverseList()

    print('\nLL after reverse():')
    my_linked_list.printLL()
    print(my_linked_list.head.value)
    print(my_linked_list.tail.value)

    my_linked_list.removeNode(2)
    my_linked_list.removeNode(3)
    my_linked_list.removeNode(4)


    print('\nLL after removeNode():')
    my_linked_list.printLL()


    my_linked_list.reverseList()
    
    print('\nLL after reverse():')
    my_linked_list.printLL()
    print(my_linked_list.head.value)
    print(my_linked_list.tail.value)

    my_linked_list.pop()
    print('\nLL after pop():')
    my_linked_list.printLL()
    print(my_linked_list.head.value)
    print(my_linked_list.tail.value)


if __name__ == "__main__": 
    main()



    