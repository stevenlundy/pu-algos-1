from random import random

def shuffle(arr):
  for i in range(1, len(arr)):
    pick = int(random()*(i + 1))
    swap(arr, i, pick)

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
