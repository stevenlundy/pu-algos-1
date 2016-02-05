class Queue:
  def __init__(self, capacity=1):
    self.head = 0
    self.tail = 0
    self.resize(capacity)

  def enqueue(self, item):
    self.storage[self.tail % self.capacity] = item
    self.tail += 1
    if self.size() == self.capacity:
      self.resize(2 * self.capacity)

  def dequeue(self):
    if self.size() > 0:
      value = self.storage[self.head % self.capacity]
      self.head += 1
      if self.size() <= 0.25 * self.capacity:
        self.resize(0.5 * self.capacity)
      return value

  def size(self):
    return self.tail - self.head

  def resize(self, capacity):
    self.capacity = int(capacity)
    new_storage = [] + [None] * self.capacity
    for i, j in enumerate(range(self.head, self.tail)):
      new_storage[i] = self.storage[j]
    self.storage = new_storage
    self.tail = self.size()
    self.head = 0
