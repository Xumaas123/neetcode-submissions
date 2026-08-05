class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        R = []
        for i in nums : 
            if i in count : 
                count[i] += 1
            else : 
                count[i] = 1
        for w in range(k) : 
            max_value = -1 
            max_count = None
            for key in count : 
                if count[key] > max_value : 
                    max_value = count[key]
                    max_count = key
            R.append(max_count)
            count[max_count] = 0 
        return R
            
