from collections import defaultdict as ddict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = ddict(int)
        for num in nums:
            n[num] += 1
            if n[num] >= 2:
                return True
        return False