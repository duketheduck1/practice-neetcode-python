class MinStack:

    def __init__(self):
        self.minS = []
        self.s=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.minS:
            self.minS.append(min(self.minS[-1], val))
        else:
            self.minS.append(val)

    def pop(self) -> None:
        if self.s:
            self.s.pop()
        if self.minS:
            self.minS.pop()
        

    def top(self) -> int:
        if self.s:
            return self.s[-1]

    def getMin(self) -> int:
        return self.minS[-1]
        
