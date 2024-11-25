def find_duplicates(nums): 
    
    _dup_list = []
    _dict = {}
    
    for each in nums: 
        
        if each in _dict and each not in _dup_list: 
            _dup_list.append(each)
            
        _dict[each] = None
        
    return _dup_list
    

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )
