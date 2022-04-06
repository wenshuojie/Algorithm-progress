# 区间加法
# 给定输入[startindex,endindex,inc]，改变数组区间内的值

class Difference:
    def __init__(self,nums) -> None:
        self.diff = [0]*len(nums)
        self.diff[0] = nums[0]
        for i in range(1,len(self.diff)):
            self.diff[i] = nums[i] - nums[i-1]

    def update(self,startindex,endindex,inc):
        self.diff[startindex] += inc
        if (endindex+1 < len(self.diff)):
            self.diff[endindex+1] -= inc
    
    def result(self):
        res = [0]*len(self.diff)
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res

def getModifiedArray(len,updates):
    array = [0]*len
    difference = Difference(array)
    for item in updates:
        difference.update(startindex = item[0],endindex = item[1],inc = item[2])
    array = difference.result()
    return array

result = getModifiedArray(5,[[1,3,2],[2,4,3],[0,2,-2]])
print(result)



