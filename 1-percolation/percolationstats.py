from percolationsimulation import PercolationSimulation
from math import sqrt

class PercolationStats:

  def __init__(self, N, T):
    self.T = T
    self.mean_value = None
    self.stddev_value = None
    self.sims = []
    for x in range(T):
      self.sims.append(PercolationSimulation(N))
    self.print_stats()

  def mean(self):
    ''' sample mean of percolation threshold'''
    if self.mean_value == None:
      sum = 0.0
      for sim in self.sims:
        sum += sim.threshold
      self.mean_value = 1.0*sum/self.T

    return self.mean_value

  def stddev(self):
    ''' sample standard deviation of percolation threshold'''
    if self.stddev_value == None:
      deviation = 0
      for sim in self.sims:
        deviation += (sim.threshold - self.mean())**2
      self.stddev_value = sqrt(deviation/(self.T - 1))

    return self.stddev_value

  def confidenceLo(self):
    ''' low  endpoint of 95% confidence interval'''
    return self.mean() - 1.96 * self.stddev() / sqrt(self.T)

  def confidenceHi(self):
    ''' high endpoint of 95% confidence interval'''
    return self.mean() + 1.96 * self.stddev() / sqrt(self.T)

  def print_stats(self):
    ci_hi = self.confidenceHi()
    ci_lo = self.confidenceLo()
    print 'mean                    = %f' % self.mean()
    print 'stddev                  = %f' % self.stddev()
    print '95%% confidence interval = %f, %f' % (ci_lo, ci_hi)

stat = PercolationStats(20, 100)
