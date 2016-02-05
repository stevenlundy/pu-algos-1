from stack_array import Stack

def parse_arithmetic(expression):
  operations = Stack()
  numbers = Stack()

  for c in expression:
    if c == '(': pass
    elif c == '+' or c == '*':
      operations.push(c)
    elif c == ')':
      operator = operations.pop()
      value2 = numbers.pop()
      value1 = numbers.pop()
      if operator == '+':
        numbers.push(value1 + value2)
      elif operator == '*':
        numbers.push(value1 * value2)
    else:
      numbers.push(int(c))

  return numbers.pop()

print parse_arithmetic('(1+((2+3)*(4*5)))')
