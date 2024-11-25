# WRITE GROUP_ANAGRAMS FUNCTION HERE #

#make a duplicate array of dictionaries 

#now take each element in the dictionary list and add it to a new list
#we call this list inner

#for each dictionary in the list, add it to add the dictionary to inner

#the go down the list and check if any other dictionary matches inner

#if yes, add that dictionary to inner
# once we have traveresed the entire list, add inner to outer
#repeat for each dictionary and once done, return outer

#returns the dict version of a string

def makeStr(dict): 

    str = ""
    _list = dict.keys()
    for each in _list: 
        str += each 

    return str

def group_anagrams(array):

    outerList = []
    _test_list = []
    
    for each in array: 
        _test_dict = {}
        for alpha in each: 
            #print(alpha)
            _test_dict[alpha] = None

        #print(_test_dict)
        _test_list.append(_test_dict)
    #print(_test_list)


    for a in range(len(_test_list)): 
        innerList = []

        if _test_list[a]:
            #print("dict: ", dict)
            #str = makeStr(_test_list[a])
            #print("str: ", str)
            innerList.append(array[a])

        
            i = a+1
            while i < len(_test_list): 
                if _test_list[i] and _test_list[i] == _test_list[a]: 
                    innerList.append((array[i]))
                    _test_list[i] = None
                
                
                i += 1

            #print(innerList)
            _test_list[a] = None 
            #print(_test_list)
            outerList.append(innerList)    

    return outerList

    ["N", "N", "tan", "N", "nat", "bat"]

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""