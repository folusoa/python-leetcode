
    
def subarray_sum(nums, target): 
    
    dict = {0: -1} 
    
    prefixSum = 0 
    for i in range(len(nums)): 
        
        prefixSum += nums[i]
        if prefixSum-target in dict: 
            index_1 = dict[prefixSum-target] + 1
            return [index_1, i]
        
        
        dict[prefixSum] = i 

    return []

def main():

    nums = [1, 2, 3, 4, 5]
    target = 9
    print ( subarray_sum(nums, target) )

    nums = [-1, 2, 3, -4, 5]
    target = 0
    print ( subarray_sum(nums, target) )

    nums = [2, 3, 4, 5, 6]
    target = 3
    print ( subarray_sum(nums, target) )

    nums = []
    target = 0
    print ( subarray_sum(nums, target) )



    """
        EXPECTED OUTPUT:
        ----------------
        [1, 3]
        [0, 3]
        [1, 1]
        []

    """

if __name__ == "__main__": 
    main()
