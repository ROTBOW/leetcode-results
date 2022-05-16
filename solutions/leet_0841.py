TITLE = 'keys and rooms'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 51 ms, faster than 99.91%
    Memory Usage: 14.4 MB, less than 54.91%
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visted, queue = set(), [0]
        for room in queue:
            for key in rooms[room]:
                if key not in visted:
                    queue.append(key)
            visted.add(room)
            
        return len(visted) == len(rooms)