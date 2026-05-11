class MinStack:

    def __init__(self):
        self.stack = []
        self.minHist = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If the min history is empty or if the current value is less
        if not self.minHist or val < self.minHist[-1]:
            self.minHist.append(val)
        else:
            self.minHist.append(self.minHist[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minHist.pop()

    def top(self) -> int:
        return(self.stack[-1])

    def getMin(self) -> int:
        return(self.minHist[-1])
