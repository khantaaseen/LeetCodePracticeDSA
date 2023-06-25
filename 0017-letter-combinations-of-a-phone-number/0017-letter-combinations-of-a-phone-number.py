class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        ans = []
        digitsString = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, currString):

            if len(currString) == len(digits):
                print("len string", len(currString))
                print("len digits", len(digits))
                print("appending", ans.append(currString))
                return 
            
            for c in digitsString[digits[i]]:
                print("currString= ", currString)
                print("i= ",i)
                print("c= ",c)
                print("dict val= ",digitsString[digits[i]])
                print("ith position of digits= ",digits[i])
                backtrack(i + 1, currString + c)
            
        if digits:
            backtrack(0, "")
        return ans