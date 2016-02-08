from random import random, shuffle

class Randomized_Queue:
  def __init__(self):
    '''construct an empty randomized queue'''
    self.front = None
    self.end = None
    self.length = 0

  def is_empty(self):
    '''is the queue empty?'''
    return self.length == 0

  def size(self):
    '''return the number of items on the queue'''
    return self.length

  def enqueue(self, item):
    '''add the item'''
    self.length += 1
    node = Node(item)
    if self.end != None:
      self.end.next = node
    else:
      self.front = node
    self.end = node

  def get_node(self, index):
    node = self.front
    for i in range(index):
      node = node.next
    return node

  def dequeue(self):
    '''remove and return a random item'''
    if self.length > 0:
      index = int(random()*self.length)
      if index == 0:
        node = self.front
        self.front = node.next
      else:
        prev = self.get_node(index - 1)
        node = prev.next
        prev.next = node.next
      self.length -= 1
      return node.value

  def sample(self):
    '''return (but do not remove) a random item'''
    if self.length > 0:
      index = int(random()*self.length)
      node = self.get_node(index)
      return node.value

  def __iter__(self):
    '''return an independent iterator over items in random order'''
    values = []
    current = self.front
    while current != None:
      values.append(current.value)
      current = current.next
    shuffle(values)
    return iter(values)

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
