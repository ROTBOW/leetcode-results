class MyQueue:

    def __init__(self):
        self.main = []
        self.sub = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        self.sub = self.main[::-1]
        ele = self.sub.pop()
        self.main = self.sub[::-1]
        return ele

    def peek(self) -> int:
        return self.main[0]

    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()