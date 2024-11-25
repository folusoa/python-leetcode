
def selection_sort(my_list):

    for each in range(len(my_list)-1): 
        #print("each: ", each)
        min_index = each 
        for next in range(each+1, len(my_list)): 
           
            if my_list[next] < my_list[min_index]: 
                min_index = next
        temp = my_list[each]
        my_list[each] = my_list[min_index]
        my_list[min_index] = temp

    return my_list 


        
def main(): 
    print(selection_sort([4,2,6,5,1,3]))

    #[3,2,6,5,1,4]
if __name__ =="__main__": 
    main()


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

