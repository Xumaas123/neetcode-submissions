class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        R = []
        for i in range(n - 1): 
            for j in range(i + 1, n): 
                R.append(arr[j])
            arr[i] = max(R)
            R = []
        arr[n - 1] = -1
        return arr