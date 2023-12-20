class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_two = [float('inf'), float('inf')]

        for choco in prices:
            if choco <= min_two[0]:
                min_two[1] = min(min_two[1], min_two[0])
                min_two[0] = choco
            elif choco <= min_two[1]:
                min_two[1] = choco
        
        if sum(min_two) > money:
            return money
        return abs(sum(min_two) - money)
                
        