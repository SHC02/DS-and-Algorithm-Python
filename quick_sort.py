'''
QuickSort

Divide and conquer

Time Complexity: O(nlogn), O(n^2) in worst case
'''
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums)//2]
    less, equal, more = [], [], []
    for i in nums:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            more.append(i)
    return quick_sort(less) + equal + quick_sort(more)

quick_sort_list = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(quick_sort_list))