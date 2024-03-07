class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        curr_idx = len(nums)-1

        for idx in range(len(nums)-1, -1, -1):
            
            if nums[idx] + idx >= curr_idx:
                curr_idx = idx
        
        return curr_idx <= 0