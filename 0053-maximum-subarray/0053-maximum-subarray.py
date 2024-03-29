class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            ans = max(ans, nums[i])
                
        return ans #if ans != float('-inf') else max(nums)