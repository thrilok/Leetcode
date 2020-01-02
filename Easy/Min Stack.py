class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        try:
            if self.s2[-1]>= x:
                self.s2.append(x)
        except:
            self.s2.append(x)

    def pop(self) -> None:
        try:
            if self.s2[-1] == self.s1[-1]:
                self.s2.pop()
        except:
            pass
        finally:
            self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        try:
            return self.s2[-1]
        except:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Runtime: 60 ms, faster than 86.11% of Python3 online submissions for Min Stack.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Min Stack.

