class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = set()
        seen = set(nums1)
        
        for arr in [set(nums2), set(nums3)]:
            for num in arr:
                if num in seen:
                    res.add(num)
                else:
                    seen.add(num)
                
        return list(res)
        