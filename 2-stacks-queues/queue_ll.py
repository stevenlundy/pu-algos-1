from linkedlist import Linkedlist

class Queue:
  def __init__(self):
    self.storage = Linkedlist()

  def enqueue(self, item):
    self.storage.add_to_tail(item)

  def dequeue(self):
    return self.storage.remove_head()

  def is_empty(self):
    return self.storage.head == None
