# 寻找数组的中心索引

def pivotIndex(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

# 使用前缀和
def pivotIndex(nums):
    total = sum(nums)
    sums = 0
    for i in range(len(nums)):
        if 2*sums+nums[i] == total:
            return i
    sums += nums[i]
    return -1