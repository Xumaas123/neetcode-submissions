class MinStack:

    def __init__(self):
        self.elements = [] # list vide

    def push(self, val: int) -> None:
        self.elements.append(val)

    def pop(self) -> None:
        self.elements.pop()
    def top(self) -> int:
        return self.elements[-1]
    def getMin(self) -> int:
        minn = self.elements[0]
        for i in range(1, len(self.elements)):
            if self.elements[i]  < minn : 
                minn = self.elements[i]
        return minn
        