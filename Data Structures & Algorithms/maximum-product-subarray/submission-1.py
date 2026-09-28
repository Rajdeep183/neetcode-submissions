class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        currmin,currmax=1,1

        for num in nums:
            tmp=currmax*num
            currmax=max(num*currmax,num*currmin,num)
            currmin=min(tmp,num*currmin,num)
            res=max(res,currmax)
        
        return res