# 冒泡排序
def bubble(nums):
    nums_len = len(nums)
    for i in range(1, nums_len):
        for j in range(nums_len-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# 选择排序
def select(nums):
    nums_len = len(nums)
    for i in range(nums_len-1):
        min_idx = i
        for j in range(i+1, nums_len):
            if nums[j] < nums[min_idx]:
                min_idx = j
        
        nums[min_idx], nums[i] = nums[i], nums[min_idx]

# 插入排序
def insert(nums):
    nums_len = len(nums)
    for i in range(1, nums_len):
        temp = nums[i]
        j = i-1
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp

def shell(nums):
    pass

# 归并排序
def mergeSort(nums, left, right):
    if left >= right:
        return
    
    mid = left + (right-left)//2
    mergeSort(nums, left, mid)
    mergeSort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    nums_len = len(nums)
    temp = [0 for _ in range(nums_len)]

    for i in range(left, right+1):
        temp[i] = nums[i]
    
    # 合并
    i, j = left, mid+1
    for k in range(left, right+1):
        if j > right or (i <= mid and j <= right and temp[j] > temp[i]):
            nums[k] = temp[i]
            i += 1
        else:
            nums[k] = temp[j]
            j += 1

# 快速排序
def quickSort(nums, left, right):
    if left >= right:
        return
    p = partition(nums, left, right)
    quickSort(nums, left, p-1)
    quickSort(nums, p+1, right)

def partition(nums, left, right):
    p = left
    i, j = p+1, right
    while i <= j:
        while i < right and nums[i] <= nums[p]:
            i += 1
        while j > left and nums[j] > nums[p]:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[p], nums[j] = nums[j], nums[p]
    return j

if __name__ == '__main__':
    test_nums = [8,4,8,2,5,0,6]
    test_nums2 = [4,5,1,6,2,7,2,8]
    # bubble(test_nums)
    # select(test_nums)
    # insert(test_nums)
    # mergeSort(test_nums2, 0, len(test_nums2)-1)
    # mergeSort(test_nums, 0, len(test_nums)-1)
    quickSort(test_nums2, 0, len(test_nums2)-1)
    quickSort(test_nums, 0, len(test_nums)-1)
    print(test_nums2)
    print(test_nums)