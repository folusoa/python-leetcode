# WRITE FIND_PAIRS FUNCTION HERE #

def find_pairs(arr1, arr2, target): 
    
    listSet = set(arr1)
    finalList = []
    
    for each in arr2: 
        
        complement = target - each 
        
        if complement in listSet: 
            newT = tuple([complement, each])
            finalList.append(newT)
            
    return finalList
            

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""