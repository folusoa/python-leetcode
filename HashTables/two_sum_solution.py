def two_sum(lst, target_sum):
    num_dict = {}
    
    for index, num in enumerate(lst):
        complement = target_sum - num
        
        if complement in num_dict:
            return [num_dict[complement], index]
        
        num_dict[num] = index

    return []  # Return an empty list if no pair is found

# Test the function to find 1 and 9
result = two_sum([1, 3, 5, 7, 9], 10)  # Looking for the pair that sums to 10
print(result)



print(two_sum([1, 3, 5, 7, 9], 10)) 