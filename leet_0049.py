TITLE = 'Group Anagrams'
'''
time: BigO(n log n)
space: BigO(n)

Results:
    Runtime: 84 ms, faster than 88.65%
    Memory Usage: 19.2 MB, less than 27.68%
'''

class Solution(object):
    def groupAnagrams(self, strs):
        keys = {}
        answer = []
        for idx, word in enumerate(strs):
            if word == '':
                if len(answer) == 0:
                    answer.append([''])
                else:
                    answer[0].append('')
                continue
                
            temp_word = sorted(word)
            word = ''.join(temp_word)
            if word not in keys:
                keys[word] = [idx]
            else:
                keys[word].append(idx)   
        
        for anas in keys.values():
            temp_list = []
            for idx in anas:
                temp_list.append(strs[idx])
            answer.append(temp_list)
        
        return answer