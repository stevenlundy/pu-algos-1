class UF:
  """initialize union find data-structure with N objects"""
  def __init__(self, N):
    self.id = range(N)

  def union(self, p, q):
    'add connection between p and q'
    qroot, qheight = self.getRoot(q)
    proot, pheight = self.getRoot(p)
    if qheight > pheight:
      self.id[proot] = qroot
    else:
      self.id[qroot] = proot

  def connected(self, p, q):
    'check whether p and q are in the same component'
    qroot, qheight = self.getRoot(q)
    proot, pheight = self.getRoot(p)
    return proot == qroot

  def getRoot(self, p):
    height = 0
    while self.id[p] != p:
      p = self.id[p]
      height += 1
    return p, height
