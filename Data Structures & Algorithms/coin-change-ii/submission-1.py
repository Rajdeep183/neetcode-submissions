class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)-1,-1,-1):
            dp0=[0]*(amount+1)
            dp0[0]=1
            for a in range(1,amount+1):
                dp0[a]=dp[a]
                if a-coins[i]>=0:
                    dp0[a]+=dp0[a-coins[i]]
            
            dp=dp0
        return dp[amount]