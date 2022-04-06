# 560. 和为 K 的子数组

class Solution:
    def subarraySum(self, nums, k):
        # sums = [0]*(len(nums)+1) # 前缀和
        sums = 0
        sums_k = {0:1}
        res = 0
        for num in nums:
            sums += num
            if sums in sums_k.keys():
                sums_k[sums] += 1
            else:
                sums_k[sums] = 1

            if (sums-k) in sums_k.keys():
                res += sums_k[sums-k]
            
        return res



# 使用defaultdict不用担心key不存在而导致报错
# from collections import defaultdict


# class Solution:
#     def subarraySum(self, nums, k):
#         pre_sum,ans = 0,0
#         map_sum = defaultdict(int)
#         map_sum[0] = 1
#         for i in range(len(nums)):
#             pre_sum += nums[i]
#             if (pre_sum-k) in map_sum:
#                 ans += map_sum[pre_sum-k]
#             map_sum[pre_sum] += 1
        
#         return ans



