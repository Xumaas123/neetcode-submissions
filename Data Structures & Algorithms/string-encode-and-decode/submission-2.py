class Solution:

    def encode(self, strs: List[str]) -> str:
        W = ""
        for string  in strs:
            W += '}' + string
        return W
    def decode(self, s: str) -> List[str]:
        s = list(s)
        T = []
        a = ""
        i = 0
        while i < len(s) :
            a = ""
            j = i + 1
            while (j < len(s) and s[j] != '}')    :
                a += s[j]
                j += 1
            T.append(a)
            i = j
        return T