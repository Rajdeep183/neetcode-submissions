class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]

        subs=self.subsets(nums[1:])
        res=[]
        for s in subs:
            res.append(s) 
            s_copy=s.copy()
            s_copy.insert(0,nums[0])
            res.append(s_copy)
        return res