def shell_sort(arr):
  h = 1
  while h < len(arr):
    h = 3*h + 1

  while h > 0:
    for i in range(0, h):
      for j in range(i, len(arr) + 1, h):
        for k in reversed(range(0, j - h, h)):
          if arr[k] > arr[k+h]:
            swap(arr, k, k+h)
          else:
            break
    h = (h - 1)/3

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
