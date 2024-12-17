class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n
        self.max_size = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.num_components -= 1
            self.max_size = max(self.max_size, self.size[rootX])


n, m = map(int, input().strip().split())
uf = UnionFind(n)
results = []

for _ in range(m):
    a, b = map(int, input().strip().split())
    uf.union(a - 1, b - 1)
    results.append(f"{uf.num_components} {uf.max_size}")

print("\n".join(results))

