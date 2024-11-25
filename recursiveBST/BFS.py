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
  
    ### WRITE BFS METHOD HERE ###
    #travers each level first 
    def BFS(self):

        node_curr = self.root

        q = []
        result = []

        if node_curr: 
            q.append(node_curr)

            while len(q) > 0:
                node_curr = q[0]

                if node_curr.left: 
                    q.append(node_curr.left)

                if node_curr.right: 
                    q.append(node_curr.right)

                result.append(q.pop(0).value)

        return result 
    

def main():

    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.BFS())



    """
        EXPECTED OUTPUT:
        ----------------
        [47, 21, 76, 18, 27, 52, 82]

    """

if __name__ == "__main__": 
    main()




                



 