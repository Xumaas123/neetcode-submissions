class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for number in numbers : 
            if (target - number) in numbers:
                value1 = target - number
                value2 = number
                break
        T = []
        for i in range(len(numbers)):
            if numbers[i] == value1 or numbers[i] == value2:
                T.append(i+1)
        return(T)