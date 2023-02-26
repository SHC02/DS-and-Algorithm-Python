'''
Merge Sort

dividing an array into smaller subarrays, 
sorting each subarray, 
and then merging the sorted subarrays back together to form the final sorted array.

process of merge sort 
    1.divide the array into two halves
    2.sort each half
    3.and then merge the sorted halves back together
This process is repeated until the entire array is sorted.

pseudocode:
    step 1: start

    step 2: declare array and left, right, mid variable

    step 3: perform merge function.
        if left > right
            return
        mid= (left+right)/2
        mergesort(array, left, mid)
        mergesort(array, mid+1, right)
        merge(array, left, mid, right)

    step 4: Stop
Time Complexity: O(nlogn)

'''
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        
        # divided into two halves
        left = nums[:mid]
        right = nums[mid:]
        
        # sort each divided parts
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        # if any element was left
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    return

merge_sort_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(merge_sort_list)
print(merge_sort_list)