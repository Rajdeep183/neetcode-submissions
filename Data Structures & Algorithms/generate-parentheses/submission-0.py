class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def backtrack(n,cur):
            left,right=cur.count("("),cur.count(")")
            if left==n and n==right:
                res.append(cur)
            if left<n:
                backtrack(n,cur+"(")
            if left>right:
                backtrack(n,cur+")")


        backtrack(n,"")
        return res

