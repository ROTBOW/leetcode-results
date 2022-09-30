class Solution:
    def is_vaild(self, pos, arr) -> bool:
        x, y = pos
        if not 0 <= x <= len(arr)-1:
            return False
        if not 0 <= y <= len(arr[0])-1:
            return False
        return True
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [[sr, sc]]
        seen = set((sr, sc))
        
        while stack:
            r, c = stack.pop()
            curr_color = image[r][c]
            
            if curr_color != color:
                for pos in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    new_r, new_c = r+pos[0], c+pos[1]
                    if self.is_vaild([new_r, new_c], image) and (new_r, new_c) not in seen:
                        seen.add((new_r, new_c))
                        if image[new_r][new_c] == curr_color:
                            stack.append([new_r, new_c])
                        
                    
                    image[r][c] = color
        return image
        