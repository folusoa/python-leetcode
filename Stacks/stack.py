class Node:

    def __init__(self, value): 
        self.value = value
        self.next = None

class Stack: 
    def __init__(self, value): 
        new_node = Node(value)
        self.top = new_node
        self.height = 1


    #return the pushed node
    def push(self, value): 

        new_node = Node(value)

        #empty stack 
        if self.height == 0: 
            self.top = new_node
        
        else:          
            new_node.next = self.top
            self.top = new_node 
        
        self.height += 1
        return self.top

    #returns the popped node 
    def pop(self): 

        #empty list
        if self.height == 0:
            return None
        

        prev = self.top 
        self.top = self.top.next
        prev.next = None
        self.height -= 1

        return prev

         


def main():

    myStax = Stack(1)
    print("after pop: ", myStax.pop().value)

    myStax.push(2)
    print("after push: ", myStax.push(2).value)



if __name__ == "__main__": 
    main()

