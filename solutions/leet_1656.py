TITLE = 'Design an Ordered Stream'
'''
time: BigO(n)
space: BigO(n)

Results:
    Runtime: 396 ms, faster than 16.40%
    Memory Usage: 14.8 MB, less than 9.09%
'''

class OrderedStream:

    def __init__(self, n: int):
        self.stream = {k: False for k in range(1, n+1)}
        self.pos = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        
        result = []
        while self.pos <= len(self.stream) and self.stream[self.pos]:
            result += [self.stream[self.pos]]
            self.pos += 1
        return result