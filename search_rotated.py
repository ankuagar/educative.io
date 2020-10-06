#!/usr/bin/env python3

import unittest
t = unittest.TestCase()
def binary_search_rotated(arr, key):

  def binary_search(arr, low, high, key):
    if low > high or (low == high and arr[low] != key):
      return -1
    mid = (low + high) // 2
#    print(low, high, key, mid)
    if arr[mid] == key:
      return mid
    elif arr[mid] < arr[high]: # if RHS is sorted
      if arr[mid] < key <= arr[high]: # key lies in sorted part
        return binary_search(arr, mid+1, high, key)
      return binary_search(arr, low, mid-1, key)
    elif arr[low] < arr[mid]: # if LHS is sorted
      if arr[low] <= key < arr[mid]: # key lies in sorted part
        return binary_search(arr, low, mid-1, key)
      return binary_search(arr, mid+1, high, key)

  return binary_search(arr, 0, len(arr)-1, key)
  
l = [176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
t.assertEqual(binary_search_rotated(l , 210), 4)

l = [7, 8, 1, 2, 4, 5, 6] 
t.assertEqual(binary_search_rotated(l , 8),1)

l = [4, 5, 6, 1, 2, 3]
t.assertEqual(binary_search_rotated(l , 6),2)
t.assertEqual(binary_search_rotated(l , 3),5)

l = [176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
t.assertEqual(binary_search_rotated(l , 211), -1)
