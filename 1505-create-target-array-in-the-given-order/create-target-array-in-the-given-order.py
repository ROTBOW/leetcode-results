class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        nums = nums[::-1]
        target = list()


        for idx in index:
            target.insert(idx, nums.pop())

        return target