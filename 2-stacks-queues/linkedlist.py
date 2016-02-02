class Linkedlist:
  def __init__(self):
    self.head = None
    self.tail = None

  def remove_head(self):
    if self.head:
      item = self.head

      if self.head == self.tail:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next

      return item.value

  def add_to_head(self, value):
    item = Node(value)

    if self.head:
      item.next = self.head
    else:
      self.tail = item

    self.head = item

  def add_to_tail(self, value):
    item = Node(value)

    if self.tail:
      self.tail.next = item
    else:
      self.head = item

    self.tail = item

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
