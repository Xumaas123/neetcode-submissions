class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        R = defaultdict(list)
        for string in strs:
            count = [0] * 26 # a ... z
            for caractere in string : 
                count[ord(caractere) - ord('a')] += 1
            R[tuple(count)].append(string)
        return(list(R.values()))