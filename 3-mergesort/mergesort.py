def mergesort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr)/2
  bottom = mergesort(arr[:mid])
  top = mergesort(arr[mid:])
  return merge(bottom, top)
  
def merge(arr1, arr2):
  i = 0
  j = 0
  merged = []
  while i < len(arr1) or j < len(arr2):
    if i >= len(arr1):
      merged.append(arr2[j])
      j += 1
    elif j >= len(arr2):
      merged.append(arr1[i])
      i += 1
    elif arr1[i] <= arr2[j]:
      merged.append(arr1[i])
      i += 1
    else:
      merged.append(arr2[j])
      j += 1
  return merged
    
print mergesort([4,1,4,2,3,0])