from stack_array import Stack

s = Stack()

print s.pop() # None
s.push('to')
s.push('be')
s.push('or')
s.push('not')
s.push('to')
print s.pop() # to
s.push('be')
print s.pop() # be
print s.pop() # not
s.push('that')
print s.pop() # that
print s.pop() # or
print s.pop() # be
s.push('is')
