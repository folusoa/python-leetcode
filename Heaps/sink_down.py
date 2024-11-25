class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    # WRITE THE _SINK_DOWN METHOD HERE #
    #takes the index of the element to sink down 
    def _sink_down(self, index):
        
        
        #while the current parent > the left child
        while True: 
            
            left = self._left_child(index)
            right = self._right_child(index)
            
            if left >= len(self.heap):
                return 
            
            if right < len(self.heap): 
                if self.heap[right] > self.heap[left] and \
                    self.heap[index] < self.heap[right]:
                    self._swap(index, right)
                    index = right
                    continue
        
            if self.heap[index] < self.heap[left]: 
                self._swap(index, left)
                index = left
                    
            else: 
                return 
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
        
        

myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(70)
myheap.insert(65)

print(myheap.heap)

myheap.remove()

print(myheap.heap)

myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""