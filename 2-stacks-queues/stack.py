from linkedlist import Linkedlist

class Stack:

  def __init__(self):
    self.storage = Linkedlist()

  def push(self, item):
    self.storage.add_to_head(item)

  def pop(self):
    return self.storage.remove_head()

  def isEmpty(self):
    return self.storage.head == None
