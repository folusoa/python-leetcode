def insertion_sort(my_list): 

    '''
    begin iterating from the second element in the list to the final elem

    for each elem that we iterate over
        while we are not at the second elem, 
            if the elem is less than the previous
                swap

            else (the curr elem is > than the previous)
                break

    first = my_list[0]
    '''
    
    for item in range(1, len(my_list)): 
        #print("item before while loop: ", item)
        while item >= 1: 
            if my_list[item] < my_list[item-1]: 
                temp = my_list[item-1]
                my_list[item-1] = my_list[item]
                my_list[item] = temp
                item -= 1

            else: 
                break

        #print("item after while loop: ", item)
    return my_list

def main(): 

    my_list = [2, 5, 1, 0, 4, 2]

    print(insertion_sort(my_list))

if __name__ == "__main__": 
    main()