
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = dict()
        count = ans = 0
        
        for i, c in enumerate(s):
            if c in cur and count <= cur[c]:
                count = cur[c] + 1
            else:
                ans = max(ans, i - count + 1)
                
            cur[c] = i
            
        return ans