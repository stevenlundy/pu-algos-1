import fileinput

k = sys.argv[1]
inputs = []
for line in fileinput.input():
  inputs.append(line)
print len(inputs)

