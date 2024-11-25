# WRITE TWO_SUM FUNCTION HERE #

def two_sum(lst, sum): 

    dict = {}
    out = []

    for index, num in enumerate(lst): 
    
        complement = sum - num
        
        if complement in lst and index != lst.index(complement): 
            #print("index: ", index, "comp: ", complement)
            out.append(index)
            out.append(lst.index(complement))
            
            return out
            #out.append(index)
            
        dict[index] = complement
        #print(dict)
        #out.append(list(dict.values()).index(complement))

    return out 

    #[0, 1, 2, 3, 4] index, key 
    #[1, 3, 5, 7, 9] num, lst
    #[9, 7, 5, 3, 1] complement, value
    '''
    for each in lst: 
        dict[each] = sum - each 

    for each in list(dict.values()):

        if each in list(dict.keys()):

            key_index = list(dict.keys()).index(each)
            value_index = list(dict.values()).index(each)
        
            if key_index != value_index: 

                out.append(lst.index(sum-each))
                out.append(lst.index(each))
                
                break

    return out
    '''
print(two_sum([5, 1, 1, 7, 2, 9, 3, 9], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )
