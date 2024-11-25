def first_non_repeating_char(string): 
    
    str_dict = {}
    
    for each in string: 
        count = 1
        if each not in str_dict: 
            str_dict[each] = count

        else: str_dict[each] += 1

    #print(str_dict)
        
    for each in str_dict: 
        if str_dict[each] == 1: 
            return each
    
    return None
    
    
    
print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('wwuhan') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""