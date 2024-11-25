class Stack: 

    '''
    implementing a stack with an empty list 
    called stack_list
    def __init__(self): 
        self.stack_list = []
    '''

    def __init__(self, value): 
        self.list = [value]
        self.top = self.list[0]
        #self.length = len(self.list)

    def push(self, value):

        #what to do if stack is empty 
        #create a new list? stack? 
        if len(self.list) == 0: 
            self.list = [value]   
        
        #stack is not empty
        else:  
            self.list.append(value) 

        '''return the index of the pushed value 
        only works well on a list with no duplicates'''
        return self.list.index(value)

    def pop(self):
        
        #empty list, nothing to pop
        if len(self.list) == 0: 
            return None
        
        #last-in, first-out - pop the last elem
        self.list.pop()
        return self.top 

    def print(self): 
        for i in range(len(self.list)):
            print(self.list[i])


def main(): 

    myStack = Stack(5)
    myStack.push(12)
    myStack.push(2)
    #print("value index: ", myStack.push(12))
    #print("value index: ", myStack.push(2))
    print(myStack.pop())
    
    print("after pop: ")
    print(myStack.print())

if __name__ == "__main__": 
    main()
