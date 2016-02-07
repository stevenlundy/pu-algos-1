class Deque:
  def __init__(self):
    '''construct an empty deque'''
    self.front = None
    self.end = None
    self.length = 0

  def is_empty(self):
    '''is the deque empty?'''
    return self.length == 0

  def size(self):
    '''return the number of items on the deque'''
    return self.length

  def add_first(self, item):
    '''add the item to the front'''
    self.length += 1
    node = Node(item)
    if self.front != None:
      self.front.prev = node
      node.next = self.front
    else:
      node.end = node
    node.front = node

  def add_last(self, item):
    '''add the item to the end'''
    self.length += 1
    node = Node(item)
    if self.end != None:
      self.end.next = node
      node.prev = self.end
    else:
      node.front = node
    node.end = node

  def remove_first(self):
    '''remove and return the item from the front'''
    if self.front != None:
      item = self.front.value
      if self.front == self.end:
        self.front = None
        self.end = None
      else:
        self.front = self.front.next
        self.front.prev = None
      self.length -= 1

  def remove_last(self):
    '''remove and return the item from the end'''
    if self.end != None:
      item = self.end.value
      if self.front == self.end:
        self.front = None
        self.end = None
      else:
        self.end = self.end.prev
        self.end.next = None
      self.length -= 1

  def __iter__(self):

  def next(self):

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
