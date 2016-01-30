from weightedquickunion import UF

uf = UF(10)
uf.union(4, 3)
uf.union(3, 8)
uf.union(6, 5)
uf.union(9, 4)
uf.union(2, 1)
print uf.connected(8, 9)
uf.union(5, 0)
uf.union(7, 2)
uf.union(6, 1)
print uf.connected(1, 0)
print uf.connected(6, 7)
