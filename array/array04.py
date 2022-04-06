# 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right

class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = []
        self.sums.append(0)
        for i in range(len(nums)):
            self.sums.append(self.sums[-1]+nums[i])


    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]