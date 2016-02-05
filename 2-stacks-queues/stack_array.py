class Stack:
  def __init__(self, capacity = 1):
    self.storage = []

    self.top = 0
    self.resize(capacity)

  def push(self, value):
    self.storage[self.top] = value
    self.top += 1
    if self.top == self.capacity:
      self.resize(2*self.capacity)

  def pop(self):
    if not self.is_empty():
      self.top -= 1
      value = self.storage[self.top]
      if self.top <= 0.25 * self.capacity:
        self.resize(0.5 * self.capacity)
      return value

  def is_empty(self):
    return self.top == 0

  def resize(self, capacity):
    self.capacity = int(capacity)
    new_storage = [] + [None] * self.capacity
    for i in range(self.top):
      new_storage[i] = self.storage[i]
    self.storage = new_storage
