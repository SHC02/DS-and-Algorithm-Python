import time
'''
Bubble Sort
'''
# Bubble Sort
def bubble_sort(nums):
    swapped = False
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                swapped = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if not swapped:
            swapped = False

bubble_sort_list = [29, 10, 14, 37, 14]
bubble_sort(bubble_sort_list)
print("Bubble Sort: ", bubble_sort_list)