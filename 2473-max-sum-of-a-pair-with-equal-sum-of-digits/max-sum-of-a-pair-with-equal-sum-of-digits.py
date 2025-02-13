from collections import defaultdict as ddict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        pairs = ddict(lambda: [0, 0])
        for idx, num in enumerate(nums):
            count = 0
            while num > 9:
                count += num % 10
                num //= 10
            count += num

            if pairs[count][0] < nums[idx]:
                pairs[count][1] = pairs[count][0]
                pairs[count][0] = nums[idx]
            
            elif pairs[count][1] < nums[idx]:
                pairs[count][1] = nums[idx]

        print(pairs)
        res = 0
        for group in pairs.values():
            if all(group):
                res = max(res, sum(group))

        return res if res != 0 else -1