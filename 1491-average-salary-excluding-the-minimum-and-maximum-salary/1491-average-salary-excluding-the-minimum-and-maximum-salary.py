class Solution:
    def average(self, salary: List[int]) -> float:
        maxi, mini = float('-inf'), float('inf')
        for num in salary:
            maxi = max(maxi, num)
            mini = min(mini, num)
        
        return (sum(salary)-(maxi+mini)) / ( len(salary)-2 )