class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers, target)
        l = 0
        r = len(numbers)-1

        while l < r:
            res = numbers[l] + numbers[r]
            if res == target:
                return [l+1, r+1]

            if res < target:
                l += 1
            else:
                r -= 1