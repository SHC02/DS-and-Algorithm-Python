'''
Insertion Sort
Time Complexity: O(N^2) 
'''
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]

        # Move elements that greater than key, to one position ahead of their current position
        j = i-1

        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        
        nums[j+1] = key
    return 

insertion_sort_list = [12,11,13,5,6]
insertion_sort(insertion_sort_list)
print(insertion_sort_list)