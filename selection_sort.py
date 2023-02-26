import time
'''
   Selection Sort
   Selection sort works by finding the minimum element and then inserting it in its correct position by swapping with
   the element which is in the position of this minimum element, and this is what makes it unstable.
   '''
# Selection sort
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

selection_sort_list = [29, 10, 14, 37, 14]
selection_sort(selection_sort_list)
print("Selection Sort: ", selection_sort_list)