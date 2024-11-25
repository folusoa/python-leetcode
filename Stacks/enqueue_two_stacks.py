class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    #works by putting the newest elem at the bottom of the stack
    # this way LILO, FIFO     
    # WRITE ENQUEUE MEHTOD HERE #
    def enqueue(self, value):
        
        #add to stack1 if it is empty else move
        #all elem of stack1 to stack2 temp 
        for each in range(len(self.stack1)): 
            self.stack2.append(self.stack1.pop())

        #add new value to stack1 
        self.stack1.append(value)

        #move all elem of stack2 back to stack1
        for each in range(len(self.stack2)): 
            self.stack1.append(self.stack2.pop())
        

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""
