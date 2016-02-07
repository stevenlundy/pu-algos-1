def insertion_sort(arr):
  for i in range(1, len(arr)):
    for j in reversed(range(0, i)):
      if arr[j] > arr[j+1]:
        swap(arr, j, j+1)
      else:
        break

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
