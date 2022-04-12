# 704. 二分查找

from typing import List

def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)-1 # 搜索区间[**]

    while(left <= right):
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid-1

    return -1

print(search([-1,0,3,5,9,12],9))
print(search([-1,0,3,5,9,12],2))
