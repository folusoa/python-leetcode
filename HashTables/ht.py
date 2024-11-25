class HashTable:
    
    def __init__(self): 
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

    def set_item(self, key, value): 
        
        index = self.__hash(key)
        
        if self.data_map[index] is None: 
            self.data_map[index] = []
            
        self.data_map[index].append([key, value])

    
    def get_item(self, key): 
    
        index = self.__hash(key)
        
        if self.data_map[index] is not None: 
            for each in range(len(self.data_map[index])): 
                if self.data_map[index][each][0] == key: 
                    return self.data_map[index][each][1]
                    
        return None

    def keys(self): 
    
        all_keys = []
        
        for index in self.data_map: 
            if index is not None: 
                for key in index: 
                    all_keys.append(key[0])
                    
        return all_keys
    

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

'''
print('Bolts:', my_hash_table.get_item('bolts'))
print('Washers:', my_hash_table.get_item('washers'))
'''
#print('Lumber:', my_hash_table.get_item('lumber'))
print(my_hash_table.keys())


#my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""