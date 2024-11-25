## WRITE MERGE FUNCTION HERE ##
def merge(srtd_lst1, srtd_lst2): 

    i = j = 0
    combined = []
    
    if not (len(srtd_lst1) and len(srtd_lst2)): 
        combined = srtd_lst1
        if not combined: 
            combined = srtd_lst2
        return combined    

    while i < len(srtd_lst1) and j < len(srtd_lst2): 

        if srtd_lst1[i] < srtd_lst2[j]: 
            if srtd_lst1[i] not in combined: 
                combined.append(srtd_lst1[i])
            i += 1

        elif srtd_lst1[i] > srtd_lst2[j]: 
            if srtd_lst2[j] not in combined: 
                combined.append(srtd_lst2[j])
            j += 1

        else:
            #combined.append(srtd_lst1[i])
            if srtd_lst2[j] not in combined: 
                combined.append(srtd_lst2[j])
            i += 1
            j += 1

    if i < len(srtd_lst1):
        for ea in range(i, len(srtd_lst1)): 
            if srtd_lst1[ea] not in combined: 
                combined.append(srtd_lst1[ea])
    elif j < len(srtd_lst2): 
        for ea in range(j, len(srtd_lst2)): 
            if srtd_lst2[ea] not in combined: 
                combined.append(srtd_lst2[ea])
    
    return combined

print(merge([1,2,3,4,4,4,4], [0, 1, 2, 3, 4, 5]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
    
 """