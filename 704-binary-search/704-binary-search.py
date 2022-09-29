class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        mid = len(nums) // 2
        
        
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return self.search(nums[:mid], target)
        else:
            test_case = self.search(nums[mid:], target)
            if test_case != -1:
                return mid + self.search(nums[mid:], target)
            else:
                return -1