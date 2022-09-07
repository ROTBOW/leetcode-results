class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        arr = []
        idx = 0
        num = 1
        while idx <= len(target)-1 and num <= n:
            arr.append(num)
            res.append('Push')
            num += 1
            if arr[-1] == target[idx]:
                idx += 1
            else:
                res.append('Pop')
                arr.pop()   
            
        return res
        