from queue_array import Queue

q = Queue()

print q.dequeue() # None
q.enqueue('to')
q.enqueue('be')
q.enqueue('or')
q.enqueue('not')
q.enqueue('to')
print q.dequeue() # to
q.enqueue('be')
print q.dequeue() # be
print q.dequeue() # or
q.enqueue('that')
print q.dequeue() # not
print q.dequeue() # to
print q.dequeue() # be
q.enqueue('is')
