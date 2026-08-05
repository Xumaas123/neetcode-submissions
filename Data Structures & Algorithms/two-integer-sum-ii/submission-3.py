class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indice = {}
        R = []
        for i in range(len(numbers)) :
            indice[i + 1] = numbers[i]
        for i in indice :
            if  i not in R :
                rest = target -  indice[i]
                if rest in indice.values() :
                    for j in indice :
                        if j > i :
                            if indice[j] == rest:
                                R.append(i)
                                R.append(j)
        return R
                            