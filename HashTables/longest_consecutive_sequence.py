def longest_consecutive_sequence(list): 
    
    if not list: 
        return 0
    
    data_set = set()
    for each in list: 
    
        data_set.add(each)
        
    longest = 1
    maxx = longest
    for each in list: 
        longest = 1
        if each-1 in data_set: 
            continue
        
        val = each+1
        while val in data_set: 
            longest+=1
            val+=1
            
        if longest > maxx: 
            maxx = longest

    return maxx


print( longest_consecutive_sequence([100, 4, 1, 99, 3, 2, 101, 102, 105, 104, 106, 107, 108]) )
