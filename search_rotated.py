#!/usr/bin/env python3
def binary_search_rotated(arr, key):
      
  def binary_search(arr, low, high, key):
    if low > high:
      return -1
    mid = (low + high) // 2
    if arr[mid] > key:
      return binary_search(arr, low, mid-1, key)
    elif arr[mid] < key:
      return binary_search(arr, mid+1, high, key)
    else:
      return mid

  def find_boundary(arr, low, high):
    if low == high:
      return low 
    mid = (low + high) // 2
    if arr[mid] > arr[mid+1]:
      return mid
    elif arr[mid] < arr[mid-1]: 
      return mid
    elif arr[mid] < arr[low]: # boundary is on the left hand side
      return find_boundary(arr, low, mid-1)
    elif arr[mid] > arr[high]: # boundary is on the right hand side
      return find_boundary(arr, mid+1, high)
    else:
       pass # control should not reach here

  boundary_idx = find_boundary(arr, 0, len(arr) - 1)
  if arr[boundary_idx] > arr[boundary_idx + 1]:
     low1, high1, low2, high2 = 0, boundary_idx, boundary_idx + 1, len(arr) - 1
  else:
     low1, high1, low2, high2 = 0, boundary_idx-1, boundary_idx, len(arr) - 1

  mid = binary_search(arr, low1, high1, key)
  if mid == -1:
    return binary_search(arr, low2, high2, key)
  else:
    return mid

l = [176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
print(binary_search_rotated(l , 210))

l = [7, 8, 1, 2, 4, 5, 6] 
print(binary_search_rotated(l , 8))

l = [4, 5, 6, 1, 2, 3]
print(binary_search_rotated(l , 6))