TITLE = 'sort array by parity II'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 276 ms, faster than 28.91%
    Memory Usage: 16.1 MB
'''
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        queue = [] + nums
        answer = []

        for number in queue:
            if number % 2 == 0 and len(answer) % 2 == 0:
                answer.append(number)
            elif number % 2 != 0 and len(answer) % 2 != 0:
                answer.append(number)
            else:
                queue.append(number)

        return answer