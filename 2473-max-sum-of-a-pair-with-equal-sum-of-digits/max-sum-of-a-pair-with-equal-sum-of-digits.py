from collections import defaultdict as ddict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        pairs = ddict(int)        
        res = 0

        for idx, num in enumerate(nums):
            count = 0
            while num > 9:
                count += num % 10
                num //= 10
            count += num

            # check if the count is already in the dict
            if count not in pairs:
                pairs[count] = idx
            else:
                # Get the total sum and check it against res
                res = max(res, nums[idx] + nums[pairs[count]])

                # then get the biggest of the two and have that one live in the dict
                if nums[pairs[count]] < nums[idx]:
                    pairs[count] = idx

        return res if res != 0 else -1