class Percolation:

  def __init__(self, N):
    self.N = N
    self.grid = []
    # set virtual top
    self.grid.append([])
    self.grid[0].append((0, 0))
    # set grid
    for i in range(1, N + 1):
      self.grid.append([])
      for j in range(N):
        self.grid[i].append((i, j))
    # set virtual bottom
    self.grid.append([])
    self.grid[N + 1].append((N + 1, 0))

  def isOpen(self, i, j):
    return self.grid[i][j] != (i, j)

  def open(self, i, j):
    # connect up
    if i - 1 > 0 and self.isOpen(i - 1, j):
      self.connect(i, j, i - 1, j)
    elif i - 1 == 0:
      self.connect(i, j, 0) # connect to virtual top
    # connect down
    if i + 1 <= self.N and self.isOpen(i + 1, j):
      self.connect(i, j, i + 1, j)
    elif i + 1 == self.N + 1:
      self.connect(i, j, self.N + 1) # connect to virtual bottom
    # connect left
    if j - 1 >= 0 and self.isOpen(i, j - 1):
      self.connect(i, j, i, j - 1)
    # connect right
    if j + 1 < self.N and self.isOpen(i, j - 1):
      self.connect(i, j, i, j + 1)

  def percolates(self):
    return self.getRoot(0, 0) == self.getRoot(self.N + 1, 0)

  def getRoot(self, i, j):
    while self.grid[i][j] != (i, j):
      i, j = self.grid[i][j]
    return (i, j)

  def connect(self, p_i, p_j, q_i, q_j = 0):
    p_root = self.getRoot(p_i, p_j)
    q_root = self.getRoot(q_i, q_j)

    self.grid[p_root[0]][p_root[1]] = q_root
