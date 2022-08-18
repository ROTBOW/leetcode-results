from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        size = count.total()
        answer = 0
        item = 0
        for k, v in count.most_common():
            item += v
            answer += 1
            if item >= (size//2):
                break
                
        return answer