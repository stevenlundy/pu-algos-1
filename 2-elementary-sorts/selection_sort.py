def selection_sort(arr):
  for i in range(len(arr)):
    min = i
    for j in range(i, len(arr)):
      if arr[j] < arr[min]:
        min = j
    swap(arr, i, min)

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
