# 34. 在排序数组中查找元素的第一个和最后一个位置

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1,-1]
    
    index = []
    left,right = 0, len(nums)

    while(left < right):
        mid = left + (right-left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid

    if left < len(nums) and nums[left] == target:
        index.append(left)
    else:
        index.append(-1)

    left,right = 0, len(nums)
    while(left < right):
        mid = left + (right-left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid

    if left-1 < len(nums) and nums[left-1] == target:
        index.append(left-1)
    else:
        index.append(-1)

    return index

print(searchRange([5,7,7,8,8,10],8))
print(searchRange([5,7,7,8,8,10],6))
print(searchRange([2,2],3))




