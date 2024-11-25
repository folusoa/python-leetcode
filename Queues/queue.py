class Node: 

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue: 

    def __init__(self, value): 
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node
        self.length = 1

    #add an element to queue add the end of the list 
    def enqueue(self, value): 

        new_node = Node(value)
        if self.length == 0:
            self.first = new_node 
            self.last = new_node
        
        else: 
            self.last.next = new_node 
            self.last = new_node

        self.length += 1
        return self.last
    
    def dequeue(self): 
        
        #empty queue 
        if self.length == 0: 
            return None
        
        prev = self.first 
        if self.length == 1: 
            self.first = None
            self.last = None 
        
        else:     
            self.first = self.first.next
            prev.next = None

        self.length -= 1
        return prev 
    
    def print(self):        
        curr = self.first
        index = 0
        while curr != None:
            index += 1
            print("index: ", index, "curr.value: ", curr.value)
            curr = curr.next


def main(): 
    
    dq = Queue(20)
    #dq.enqueue(12)
    #dq.enqueue(30)
    print("after in_queue: ")
    print(dq.print())
    print("queue length: ", dq.length)

    dq.dequeue()
    print("after dequeue: ")
    print(dq.print())

    print("queue length: ", dq.length)
    
    

if __name__ == "__main__": 
    main()