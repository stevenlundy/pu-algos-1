from percolation import Percolation

perc = Percolation(4)
perc.open(1,0)
perc.open(2,0)
perc.open(3,0)
print perc.percolates()
perc.open(4,0)
print perc.percolates()
