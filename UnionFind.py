class UnionFind:
    """
    Dynamic union find implementation with:
      - Path compression
      - Rank based union
    If size is known upfront, change p, rank to lists for better performance
    
    From: https://github.com/decimalpack/BinarySearch-utils
    """
    def __init__(self):
        self.p = {}
        self.rank = defaultdict(int)
    def find(self,x):
        x=tuple(x)
        og = x
        while x!=self.p.get(x,x):
            self.p[x]=self.p.get(self.p.get(x,x),x)
            x=self.p.get(x,x) 
        self.p[og]=x
        return x
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b: return False
        if self.rank[b]<self.rank[a]: a,b = b,a
        self.p[b]=a
        if self.rank[a]==self.rank[b]:
            self.rank[b]+=1
        return True
