class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dictionary = {}
        columnstr = ""
        for i in range(26):
            dictionary[i + 1] = chr(ord('a') + i)
        while (columnNumber > 26):
            r = columnNumber % 26
            columnNumber //= 26
            columnstr += dictionary[r]

        columnstr += dictionary[columnNumber]
        columnstr = [columnstr[i] for i in range(len(columnstr) - 1, -1, -1)]
        return ("".join(columnstr).upper())