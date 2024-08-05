from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        items = dict()
        for key, v in count.items():
            if v == 1:
                items[len(items)] = key

        return items.get(k-1, '')