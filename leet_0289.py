TITLE = 'Game of Life'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 37 ms, faster than 71.88%
    Memory Usage: 14 MB, less than 47.75%
'''

class Solution:
    
    def get_neighbor_count(self, loca, board) -> int:
        def vaild_loca(loca, board):
            row, col = loca
            if not -1 < row < len(board):
                return False
            if not -1 < col < len(board[0]):
                return False
            return True
            
        count = 0
        for move in [(1,0),(0, 1),(1, 1),(-1, 0), (0, -1),(-1, -1),(-1, 1),(1, -1)]:
            new_loca = [ loca[0]+move[0], loca[1]+move[1] ]
            if vaild_loca(new_loca, board):
                if board[new_loca[0]][new_loca[1]] == 1:
                    count += 1
        return count
    
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        life = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                neighbor_count = self.get_neighbor_count([row, col], board)
                if neighbor_count < 2 or neighbor_count > 3:
                    life.add((row, col, 0))
                elif 2 <= neighbor_count <= 3:
                    if board[row][col] == 0 and neighbor_count == 2:
                        life.add((row, col, 0))
                    else:
                        life.add((row, col, 1))
        for row, col, val in life:
            board[row][col] = val