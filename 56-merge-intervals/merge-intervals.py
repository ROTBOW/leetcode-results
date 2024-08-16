class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we to sort our intervals
        # when we sort, reverse it
        # and I do this, so I treat it like a stack
        # create a var res, this will be what we return

        # while our stack (intervals) has at least 1 interval - which means our will end when there is only one left
        #   if the curr top of stack can merged with what is directly below it, we merge them to the one below it, and pop off the top
        #   else pop off the top and append to res

        # when our loop ends we're return rez + intervals
        intervals.sort(reverse=True)
        res = list()

        while len(intervals) > 1:
            top = intervals.pop()
            if top[1] >= intervals[-1][0]: # this is the care we merge
                intervals[-1][0] = min(intervals[-1][0], top[0])
                intervals[-1][1] = max(intervals[-1][1], top[1])
            else: # so we can't merge
                res.append(top)

        return res + intervals