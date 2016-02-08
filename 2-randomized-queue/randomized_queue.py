class Randomized_Queue:
  def __init__(self):
    '''construct an empty randomized queue'''

  def isEmpty(self):
    '''is the queue empty?'''

  def size(self):
    '''return the number of items on the queue'''

  def enqueue(self, item):
    '''add the item'''

  def dequeue(self):
    '''remove and return a random item'''

  def sample(self):
    '''return (but do not remove) a random item'''

  def __iter__(self):
    '''return an independent iterator over items in random order'''
    return self

  def next(self):
    return self
