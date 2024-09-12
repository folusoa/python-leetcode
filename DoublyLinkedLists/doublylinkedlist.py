#doubly linked list 
class Node: 
    def __init__(self, value):
        #print("did we get here? Node")
        self.value = value
        self.next = None
        self.prev = None 

#should add a node to the list
#remove a node from the end of the list
class DoublyLinkedList:   

    #to be called only when creating a new Linked List 
    #assigns head to the first node created
    def __init__(self, value): 
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode 
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #add an element to the end of the list 
    def append(self, value):

        newNode = Node(value)

        if self.length == 0: 
            self.head = newNode
            self.tail = newNode

        else: 
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

        self.length += 1
        return True #??
    
    #remove an element from the end of the list
    def pop(self): 

        #empty list
        if self.length == 0: 
            return None
        
        #single node
        if self.length == 1: 
            temp = self.tail
            self.head = self.tail = None 
            self.length -= 1
            return temp
        
        ptr = self.tail
        self.tail = ptr.prev
        self.tail.next = None
        ptr.prev = None 
        self.length -= 1
        return ptr 

    #inserts a new node at the beginning of the list
    def prepend(self, value): 

        newNode = Node(value)

        if self.length == 0: 
            self.head = newNode
            self.tail = newNode

        else: 
            newNode.next = self.head 
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return True
    
    #remove the first element in a list
    def pop_first(self): 

        if self.length == 0: 
            return None
        
        temp = self.head
        if self.length == 1: 
            self.head = self.tail = None
            
        else: 
            self.head = temp.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp


    def get(self, index):
        
        if index < 0 or index >= self.length:
            return None 
            
        if index < self.length/2:
            itr = self.head
            for i in range(index): 
                itr = itr.next
            return itr

        elif index >= self.length/2: 
            itr = self.tail
            for i in range(self.length-1, index, -1): 
                itr = itr.prev
            return itr
        
    
    def set_value(self, index, value): 
        
        temp = self.get(index)

        if temp: 
            temp.value = value
            return True 
        
        return False


    #insert an node at a given index
    def insert(self, index, value):

        if index < 0 or index > self.length:
            return False 
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        newNode = Node(value)

        before = self.get(index-1)
        after = before.next 

        before.next = newNode
        newNode.prev = before
        newNode.next = after
        after.prev = newNode
        self.length += 1
        return True


    #remove the node at a given index
    def remove(self, index):

        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length-1:
            return self.pop()

        before = self.get(index-1)
        node = before.next 
        after = node.next
        
        before.next = after
        after.prev = before
        node.next = node.prev = None

        self.length -= 1
        return node

def main(): 

    mydLL = DoublyLinkedList(4)
    mydLL.append(5)
    mydLL.prepend(8)

    print("current list: ")
    mydLL.print_list()

    mydLL.get(3)
    mydLL.set_value(3, 9)
    mydLL.pop_first()
    mydLL.pop()
    mydLL.insert(0, 10)

    print("\n")
    print("list after changes: ")
    mydLL.print_list()


if __name__ == "__main__": 
    main()