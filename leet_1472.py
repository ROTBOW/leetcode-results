'''
leet_1472 is asking to create a small browser history.
Instead of stacks, I used a list and a pointer. The list housing
all the urls and the pointer showing where we are in the history.

Time: BigO(1)
Space: BigO(n)
'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_idx = 0
        self.size = 1
        

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curr_idx+1]
        self.history.append(url)
        self.size = len(self.history)
        self.curr_idx = self.size-1

    def back(self, steps: int) -> str:
        print(self.history)
        if self.curr_idx - steps <= 0:
            self.curr_idx = 0
            return self.history[0]
        self.curr_idx = self.curr_idx - steps
        return self.history[self.curr_idx]
        

    def forward(self, steps: int) -> str:
        if self.curr_idx + steps > self.size-1:
            self.curr_idx = self.size-1
            return self.history[self.size-1]
        self.curr_idx = self.curr_idx + steps
        return self.history[self.curr_idx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)