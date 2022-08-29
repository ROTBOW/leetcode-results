class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        temp_str = ''
        for letter in s:
            temp_str += letter
            if len(temp_str) == k:
                answer.append(temp_str)
                temp_str = ''
                
        while temp_str and len(temp_str) < k:
            temp_str += fill
        
        return answer + [temp_str] if temp_str else answer