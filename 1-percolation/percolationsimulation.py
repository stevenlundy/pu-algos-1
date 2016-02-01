from percolation import Percolation
from random import random

class PercolationSimulation:

  def __init__(self, N):
    self.visual_grid = self.make_empty_grid(N)
    self.perc = Percolation(N)
    self.N = N
    self.to_open = range(N**2)
    self.open_sites = 0
    self.run_simulation()

  def make_empty_grid(self, N):
    grid = []
    for i in range(N):
      grid.append([])
      for j in range(N):
        grid[i].append('0')
    return grid

  def print_grid(self, grid):
    print('\n'.join(''.join(x) for x in grid))

  def open_next_block(self):
    next_index = int(random()*len(self.to_open))
    next = self.to_open[next_index]
    del self.to_open[next_index]
    i = int(next/self.N + 1)
    j = next%self.N
    self.perc.open(i, j)
    self.visual_grid[i-1][j] = ' '
    self.open_sites += 1

  def run_simulation(self):
    while not self.perc.percolates():
      self.open_next_block()
    self.print_grid(self.visual_grid)
    self.threshold = 1.0*self.open_sites/self.N**2


sim = PercolationSimulation(20)
print sim.threshold
