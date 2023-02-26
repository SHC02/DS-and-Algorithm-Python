import time
'''
1. declare low, mid, high positions
2. create a while loop that compare mid values to low and high value
3. if mid element of the array is lower than target, increment low
4. if mid element of the array is bigger than target, decrement high
5. otherwise, the option is middle
6. if error occurs, return -1
'''

# Binary Search
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

arr = [2, 3, 4, 10, 40]
print(binary_search(arr, 40))