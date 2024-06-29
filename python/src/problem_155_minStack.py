# https://leetcode.com/problems/min-stack


class MinStack:
    def __init__(self) -> None:
        self._vals = []
        self._mins = []

    def push(self, val: int) -> None:
        self._vals.append(val)
        if len(self._mins) == 0:
            self._mins.append(val)
            return
        self._mins.append(min(val, self._mins[-1]))

    def pop(self) -> None:
        self._vals.pop()
        self._mins.pop()

    def top(self) -> int:
        return self._vals[-1]

    def getMin(self) -> int:
        return self._mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
