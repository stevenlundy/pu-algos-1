class Stack:
  def __init__(self, size):
    self.storage = [] + [None] * size
    self.top = 0

  def push(self, value):
    self.storage[self.top] = value
    self.top += 1

  def pop(self):
    if not self.is_empty():
      self.top -= 1
      return self.storage[self.top]

  def is_empty(self):
    return self.top == 0
