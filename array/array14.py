# 搜索左（右）侧边界

from typing import List

def left_bound(nums: List[int], target: int) -> int:
    left,right = 0,len(nums) # 搜索区域[**)

    while(left < right):
        mid = left + (right-left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid
    
    return left if nums[left] == target and left < len(nums) else -1

print(left_bound([1,2,2,2,3],2))

def right_bound(nums:List[int],target:int) -> int:
    left,right = 0,len(nums) # 搜索区间[**)

    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            left = mid+1
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid

    return left-1 if nums[left-1] == target and left-1 < len(nums) else -1 # 终止条件是left==right，且nums[mid] == target时，left=mid+1

print(right_bound([1,2,2,2,3],2))
print(right_bound([2,2],3))
        
