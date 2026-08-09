class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_wrd = ""
        len_max = min(len(word1), len(word2))
        for i in range(len_max):
            new_wrd += word1[i]
            new_wrd += word2[i]
        if max(len(word1), len(word2)) == len(word1):
            for i in range(len_max, len(word1)):
                new_wrd += word1[i] 
        else:
            for i in range(len_max, len(word2)):
                new_wrd += word2[i]
        return(new_wrd)