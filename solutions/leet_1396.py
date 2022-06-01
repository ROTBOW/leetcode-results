TITLE = 'Design underground system'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 261 ms, faster than 80.44%
    Memory Usage: 23.4 MB, less than 99.59%
'''
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.times = defaultdict(list)
        self.starts = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.starts[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.starts[id]
        self.times[f'{start[0]}_{stationName}'].append(t - start[1])
        del self.starts[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.times[f'{startStation}_{endStation}']
        return sum(time) / len(time)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)