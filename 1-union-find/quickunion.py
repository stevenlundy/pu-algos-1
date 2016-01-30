class UF:
  """initialize union find data-structure with N objects"""
  def __init__(self, N):
    self.id = range(N)

  def union(self, p, q):
    'add connection between p and q'
    qroot = self.getRoot(q)
    proot = self.getRoot(p)
    self.id[proot] = qroot

  def connected(self, p, q):
    'check whether p and q are in the same component'
    return self.getRoot(p) == self.getRoot(q)

  def getRoot(self, p):
    if self.id[p] == p:
      return p
    else:
      return self.getRoot(self.id[p])
