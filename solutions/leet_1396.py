TITLE = 'Design underground system'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 252 ms, faster than 88.77%
    Memory Usage: 23.6 MB, less than 95.21%
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
        if f'{start[0]}_{stationName}' not in self.times:
            self.times[f'{start[0]}_{stationName}'].append(t - start[1])
            self.times[f'{start[0]}_{stationName}'].append(1)
        else:
            self.times[f'{start[0]}_{stationName}'][0] += t - start[1]
            self.times[f'{start[0]}_{stationName}'][1] += 1
        del self.starts[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.times[f'{startStation}_{endStation}']
        return time[0] / time[1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)