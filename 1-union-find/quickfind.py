class UF:
  """initialize union find data-structure with N objects"""
  def __init__(self, N):
    self.id = range(N)

  def union(self, p, q):
    'add connection between p and q'
    old_group = self.id[q]
    new_group = self.id[p]
    for id in range(len(self.id)):
      if self.id[id] == old_group:
        self.id[id] = new_group

  def connected(self, p, q):
    'check whether p and q are in the same component'
    return self.id[p] == self.id[q]
