class UnionFind:
    """
    Dynamic union find implementation (Size unknown) with:
      - Path compression
      - Rank based union
    
    
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
        if self.rank[a]<self.rank[b]: a,b = b,a
        self.p[b]=a
        if self.rank[a]==self.rank[b]:
            self.rank[b]+=1
        return True
class UnionFind:
    """
    Static union find implementation (Size known, 0 indexed) with:
      - Path compression
      - Rank based union
    
    From: https://github.com/decimalpack/BinarySearch-utils
    """
    def __init__(self,size):
        self.p = list(range(size))
        self.rank = [0]*size
    def find(self,x):
        while x!=self.p[x]:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b: return False
        if self.rank[a]<self.rank[b]: a,b = b,a
        self.p[b]=a
        if self.rank[a]==self.rank[b]:
            self.rank[b]+=1
        return True
