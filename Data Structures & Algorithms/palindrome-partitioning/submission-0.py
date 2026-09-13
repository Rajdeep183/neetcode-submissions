class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def pal(sub):
            return sub==sub[::-1]
        def backtrack(start):
            if start==len(s):
                res.append(path.copy())
                return 

            for end in range(start+1,len(s)+1):
                sub=s[start:end]
                if pal(sub):
                    path.append(sub)
                    backtrack(end)
                    path.pop()

        backtrack(0)

        return res