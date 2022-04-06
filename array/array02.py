# 搜索插入位置
# 在一个有序数组中找第一个大于等于 target 的下标

def searchInsert(nums, target):
    n = len(nums)
    left,right,ans = 0, n-1, n

    while left <= right:
        mid = (right-left) // 2 + left
        if target <= nums[mid]:
            right = mid-1
        else:
            left = mid+1

    return left
        
print(searchInsert([1,3,5,6,8],7))      
