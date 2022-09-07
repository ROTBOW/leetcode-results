class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = [] # [1, 3] - [P, P, p]
        arr = [] # [1]
        idx = 0 # 1
        num = 1 # 3
        while idx <= len(target)-1 and num <= n:
            arr.append(num)
            res.append('Push')
            if arr[-1] == target[idx]:
                idx += 1
            else:
                res.append('Pop')
                arr.pop()
            num += 1
            
        return res
        