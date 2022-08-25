from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = Counter(nums)
        for num in n.values():
            if num >= 2:
                return True
        return False