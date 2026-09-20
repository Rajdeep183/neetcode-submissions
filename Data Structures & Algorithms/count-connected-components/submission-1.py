class DSU:
    def __init__(self,n):
        self.comps=n
        self.parent=list(range(n))
        self.size=[1]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,u,v):
        pu,pv=self.find(u),self.find(v)
        if pu==pv:
            return
        self.comps -= 1 
        if self.size[pu]<self.size[pv]:
            pu,pv=pv,pu
        self.size[pu]+=self.size[pv]
        self.parent[pv] = pu



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu=DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.comps