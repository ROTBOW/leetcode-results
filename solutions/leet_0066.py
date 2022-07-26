TITLE = 'Plus One'
'''
time: BigO(n)
space: BigO(1)

Results:
    Runtime: 43 ms, faster than 69.92%
    Memory Usage: 13.8 MB, less than 58.40%
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
                    
            else:
                digits[i] += 1
                break
                
        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # brute force
        num = int(''.join([str(x) for x in digits]))
        num += 1
        return [int(x) for x in list(str(num))]