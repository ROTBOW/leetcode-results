TITLE = 'Longest Common Prefix'
'''
time: BigO(n + m) where m is the len of the shortest word
space: BigO(n)

Results:
    Runtime: 54 ms, faster than 35.45%
    Memory Usage: 14 MB, less than 11.98%
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_len = min([len(x) for x in strs])
        results = dict()
        
        for i in range(shortest_len):
            results[i] = []
            for word in strs:
                results[i].append(word[i])
            if len(set(results[i])) != 1:
                del results[i]
                break
                    
        return ''.join([x[0] for x in results.values()])
        