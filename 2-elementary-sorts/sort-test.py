from selection_sort import selection_sort as sort
from random import shuffle

numbers = range(10000)
shuffle(numbers)
sort(numbers)

print numbers
