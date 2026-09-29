class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        # [0] is the value, [1] is the min @ that point
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            new_min = min(val, (self.stack[-1])[1])
            self.stack.append((val, new_min))
        
    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]