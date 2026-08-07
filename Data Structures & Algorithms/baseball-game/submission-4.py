class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for c in operations:
            if (c == '+'):
                record.append(int(record[-1]) + int(record[-2]))
            elif (c == 'D'):
                record.append(int(record[-1] * 2))
            elif (c == 'C'):
                record.pop()
            else:
                record.append(int(c))
        return (sum(record))