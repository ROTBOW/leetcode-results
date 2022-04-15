TITLE = 'keys and rooms'
'''
time: BigO(n)
space: BigO(n)
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