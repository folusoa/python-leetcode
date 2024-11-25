class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    '''
    ### WRITE DFS_POST_ORDER METHOD HERE ###
    def dfs_post_order(self):
        
        results = []
        stack = []
        def traverse(node):
            
            if node:
                
                if node.left: 
                    stack.append(node.left)
                    results.append(node.left.value)
                    
                if node.right: 
                    results.append(node.right.value)
                    
                #do once
                if node == self.root: 
                    results.append(node.value)
                    
                if stack: 
                    if stack[-1] == self.root: 
                        return traverse(stack.pop().right)
                        
                    return traverse(stack.pop())
                    
            return results 
                    
                
        if self.root: 
            stack.append(self.root)
            return traverse(self.root)
        
        return self.root
    '''

    def dfs_post_order(self):
        
        results = []
        def traverse(node):
            
            if node:
                
                if node.left: 
                    traverse(node.left)
                    
                if node.right: 
                    traverse(node.right)
                    
                results.append(node.value)
                    
            return results 
                              
        if self.root: 
            return traverse(self.root)
        
        return self.root

my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(6)
my_tree.insert(4)
my_tree.insert(15)
my_tree.insert(12)
my_tree.insert(5)
my_tree.insert(14)
my_tree.insert(7)

print(my_tree.dfs_post_order())

"""
    EXPECTED OUTPUT:
    ----------------
    [18, 27, 21, 52, 82, 76, 47]

 """
