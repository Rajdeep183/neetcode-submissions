class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, l: int) -> int:
        inf=float('inf')
        dist=[[inf] * n for _ in range(n)]

        for u,v,w in times:
            dist[u-1][v-1]=w
        for i in range(n):
            dist[i][i]=0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

        res=max(dist[l-1])
        return res if res<inf else -1