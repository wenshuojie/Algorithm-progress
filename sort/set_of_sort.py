def bubbleSort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr): # 控制轮数
        ex = False
        for j in range(len_arr-i): # 控制ind
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ex = True
        if not ex: # 没有交换说明已经排序完毕
            return

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        if min_ind != i:
            arr[min_ind], arr[i] = arr[i], arr[min_ind]

def insertionSort(arr):
    for i in range(1, len(arr)):
        deal = arr[i] # 待排序的数
        j = i-1 # 排好序部分的末尾
        if arr[j] > deal:
            while j >= 0 and deal < arr[j]:
                arr[j+1] = arr[j]
                j -= 1 
            arr[j+1] = deal

def mergeSort(arr, left, right):
    if left >= right:
        return
    temp = [0] * len(arr)
    mid = left + (right - left) // 2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, mid, right, temp)

def merge(arr, left, mid, right, temp):
    for i in range(left, right+1):
        temp[i] = arr[i]
    
    i, j = left, mid+1
    for k in range(left, right+1):
        if i > mid:
            arr[k] = temp[j]
            j += 1
        elif j >right:
            arr[k] = temp[i]
            i += 1
        elif temp[i] < temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1

def quickSort(arr, left, right):
    if left >= right:
        return
    p = partition(arr, left,right)
    quickSort(arr, left, p-1)
    quickSort(arr, p+1, right)

def partition(arr, left, right):
    pivot = arr[left]
    i, j = left+1, right
    while i <= j:
        while i < right and arr[i] <= pivot: # 此 while 结束时恰好 nums[i] > pivot
            i += 1
        while j > left and arr[j] > pivot: # 此 while 结束时恰好 nums[j] <= pivot
            j -= 1
        
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j

arr = [1,3,2,4,2]
quickSort(arr, 0, len(arr)-1)
print(arr)