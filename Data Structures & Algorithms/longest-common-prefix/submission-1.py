class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        preffix = strs[0]
        for mot in strs[1:]:
            i = 0
            while i < len(mot) and i < len(preffix) and mot[i] == preffix[i]:
                i += 1
            preffix = preffix[:i]
        if preffix == "":
            return preffix
        return preffix