class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class BinarySearchTree: 

    def __init__(self): 
        self.root = None

    def insert(self, value): 
        
        if self.root == None: 
            self.root = TreeNode(value)
            return self.root.value
        
        curr_node = self.root
        return self.traverse(curr_node, value)
    
    def traverse(self, node, value): 

        if node is None: 
            return TreeNode(value)
        
        if value < node.value: 
            #traverse left 
            node.left = self.traverse(node.left, value)

        if value > node.value: 
            #traverse right
            node.right = self.traverse(node.right, value)
        
        return node
    
    def printBST(self):

        visited = []
        stax = []
        
        def traverse(node): 

            if node: 
                visited.append(node.value)

                if node.left: 
                    stax.append(node)
                    return traverse(node.left)

                if node.right: 
                    return traverse(node.right)
                
                if stax: 
                    return traverse(stax.pop().right)

            #print(BST_items)
            return visited
        
        if self.root == None: 
            return self.root 
        
        node = self.root
        return traverse(node)
    
    def searchBST(self, val):
        
        #pre-order dfs
        #root, left, right 

        visited = []
        def traverse(node):

            if node: 
                #visited.append(node.val)

                if val == node.value:
                    
                    visited.append(node.value)

                    if node.left: 
                        visited.append(node.left.value)

                    if node.right: 
                        visited.append(node.right.value)
                    
                    return visited
            
                if val < node.value: 
                    return traverse(node.left)

                if val > node.value:
                    return traverse(node.right)

            return node

        if self.root == None: 
            return self.root
        
        node_curr = self.root
        return traverse(node_curr)
        
'''
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Insert into an empty tree -----\n")
bst = BinarySearchTree()
print("Inserting value:", 5)
bst.insert(5)
check(5, bst.root.value, "Root value after inserting 5:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")

print("\n----- Test: Insert values in ascending order -----\n")
bst = BinarySearchTree()
values = [1, 2, 3, 4, 5]
for val in values:
    print("Inserting value:", val)
    bst.insert(val)

# Check tree structure
check(1, bst.root.value, "Root value:")
check(2, bst.root.right.value, "Right child of root:")
check(3, bst.root.right.right.value, "Right child of right child of root:")
check(4, bst.root.right.right.right.value, "Right child's right child's right child of root:")
check(5, bst.root.right.right.right.right.value, "Fourth right child of root:")

print("\n----- Test: Insert values in descending order -----\n")
bst = BinarySearchTree()
values = [5, 4, 3, 2, 1]
for val in values:
    print("Inserting value:", val)
    bst.insert(val)

# Check tree structure
check(5, bst.root.value, "Root value:")
check(4, bst.root.left.value, "Left child of root:")
check(3, bst.root.left.left.value, "Left child of left child of root:")
check(2, bst.root.left.left.left.value, "Left child's left child's left child of root:")
check(1, bst.root.left.left.left.left.value, "Fourth left child of root:")

print("\n----- Test: Insert values in mixed order -----\n")
bst = BinarySearchTree()
values = [3, 1, 4, 5, 2]
for val in values:
    print("Inserting value:", val)
    bst.insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(1, bst.root.left.value, "Left child of root:")
check(2, bst.root.left.right.value, "Right child of left child of root:")
check(4, bst.root.right.value, "Right child of root:")
check(5, bst.root.right.right.value, "Right child of right child of root:")

print("\n----- Test: Insert duplicate values -----\n")
bst = BinarySearchTree()
values = [3, 3, 3]
for val in values:
    print("Inserting value:", val)
    bst.insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")
'''

def main(): 

    bst = BinarySearchTree()
    values = [10, 5, 3, 7, 8]
    for val in values:
        print("Inserting value:", val)
        bst.insert(val)

    print(bst.printBST())

    print(bst.searchBST(5))

if __name__ == "__main__": 
    main()