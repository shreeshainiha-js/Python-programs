def single_find(nums):
    result=0
    for num in nums:
        result^=num #perform XOR operation so that the elements occuring twice will be removed.
    return result
nums=[1,2,2,1,3,3,4]
print(single_find(nums)) #Output: 4
