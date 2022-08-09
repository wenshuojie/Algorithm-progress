# 旋转数组的最小数字

class Solution:
    def minNumberInRotateArray(self , rotateArray: List[int]) -> int:
        left, right = 0, len(rotateArray)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            if rotateArray[mid] < rotateArray[right]:
                left = mid+1
            elif rotateArray[mid] == rotateArray[right]:
                right -= 1
            else:
                right = mid
        return rotateArray[left]