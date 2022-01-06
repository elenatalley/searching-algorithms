# lst = [3, 5, 11, 12, 15, 23, 25, 34, 67, 86]
lst = [3, 5, 11, 12, 15, 3, 5, 11, 12, 15]

# target = 3
# first, last = 0, len(lst) - 1
# middle = (first - last) // 2 # find index of the mid element

# a = lst[middle] # find a number
# print(a)


def search (nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1