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
    
    #create a new Node, then add it     
    #self is a linked list
    def addValue(self, value):

        #if the list is empty
        if self.head is None: 
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            
        #the list is not empty
        else: 
            newNode = Node(value)
            curr = self.tail
            curr.next = newNode
            self.tail = newNode    

        self.length += 1

    #get an element from the linked list by it's index 
    def get(self, index): 

        #edge case: LL is empty
        if self.length == 0: 
            print("The list is empty")
            return None
        
        #make sure it is a valid index   
        if index >= 0 and index < self.length: 

            itr = self.head
            l_index = 0
            while itr is not None: 

                if l_index == index:
                    return itr.value
                
                itr = itr.next
                l_index+=1
                
            return itr
        
        else:
            print("Invalid Index")
      
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

    #remove the first node
    def popFirst(self):
        if self.length == 0: 
            return None
        
        iter = self.head
        self.head = iter.next
        iter.next = None
        self.length -= 1
        if self.length == 0: 
            self.tail == 0

    #remove a node from the end of a LL
    #we do not care about the value
    def pop(self): 

        if self.length == 0: 
            return None
        
        elif self.head == self.tail:
            self.head = self.tail = None
            self.length -= 1
        
        else:
            pre = curr = self.head

            while curr.next != None: 
                pre = curr
                curr = curr.next
            
            self.tail = pre 
            pre.next = None
            self.length -= 1
            
        return curr
    
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

              
    def printLL(self): 
        if self.length == 0:
            print("The list is empty")
        #goal is to have a pointer that inherits the same abilities as the head pointer. 
        iter = self.head
        while iter != None: 
            print (iter.value)
            iter = iter.next 

    
def main(): 

    myLinkedList = LinkedList(0)
    #myLinkedList.removeNode(0)
    #head = myLinkedList.head.value

    #print("LL head: ", head)

    for i in range(0, 6): 
        myLinkedList.addValue(i*30+i-12)

    print("linked list before removing the node")    
    myLinkedList.printLL()

    print("Length: ", myLinkedList.length)

    for each in range(0, myLinkedList.length): 
        print("value at", each,":", myLinkedList.get(each))

    #for i in range(0, myLinkedList.length): 
        #print("i: ", i)
    node = 1
    #myLinkedList.removeNode(node)   
    myLinkedList.pop()

    print("LL head: ", myLinkedList.head.value)
    print("LL tail: ", myLinkedList.tail.value)

    node = myLinkedList.tail.value
    myLinkedList.removeNode(node)

    print("LL tail after removing prev tail: ", myLinkedList.tail.value)

    node = myLinkedList.head.value
    #for i in range(0,2):
        #myLinkedList.removeNode(node)

    #print("LL head after removing prev: ", myLinkedList.head.value)

    myLinkedList.pop()
    print("linked list after removing the node")

    myLinkedList.prepend(33)
    myLinkedList.printLL()
    print("head: ", myLinkedList.head.value)

    print("LL length: ", myLinkedList.length)

    testLL = LinkedList(23)
    testLL.prepend(30)
    testLL.printLL()

    print('LL head: ', testLL.head.value)
    print('LL tail: ', testLL.tail.value)

    testLL.pop()
    testLL.popFirst()

    print("testLL after operations")
    testLL.printLL()

    testLL.get(2)

    print(myLinkedList.get(2))
    

    #print("after")
    #print('LL head: ', testLL.head.value)
    #print('LL tail: ', testLL.tail.value)
    

if __name__ == "__main__": 
    main()



    