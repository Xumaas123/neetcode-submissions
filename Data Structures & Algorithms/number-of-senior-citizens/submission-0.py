class Solution:
    def countSeniors(self, details: List[str]) -> int:
        Age_Array = []
        Age_valide = []
        for i in range (len(details)):
            age = int (details[i][11]) * 10 + int(details[i][12])
            Age_Array.append(age)
        for age in Age_Array:
            if age > 60: 
                Age_valide.append(age)
        return (len(Age_valide))