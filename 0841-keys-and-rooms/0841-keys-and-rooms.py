class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visted, stack = set(), [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visted:
                    stack.append(key)
            visted.add(room)
            
        return len(visted) == len(rooms)