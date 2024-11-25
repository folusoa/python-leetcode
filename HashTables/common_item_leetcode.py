# WRITE ITEM_IN_COMMON FUNCTION HERE #

def item_in_common(list1, list2): 
    
    myDict = {}
    
    for each in list1: 
        myDict[each] = None
        
    for each in list2: 
        if each in myDict: 
            return True 
            
        myDict[each] = None
    
    return False


list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))
