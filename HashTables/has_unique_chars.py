
def has_unique_chars(string): 
    
    string_set = set()
    
    for each in string: 
        
        if each in string_set: 
            return False
            
        string_set.add(each)
    
    return True

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False