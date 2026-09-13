class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dict1={
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        def backtrack(i, st):
            if len(st)==len(digits):
                res.append(st)
                return
            for c in dict1[digits[i]]:
                backtrack(i+1,st+c)
        if digits:
            backtrack(0,"")
        return res        

            
