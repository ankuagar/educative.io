#!/usr/bin/env python3
import unittest
t = unittest.TestCase()
def find_sum_of_two(A, val):
    '''
    O(N)
    use extra space
    '''
    s = set()
    for item in A:
        if (val - item) in s:
            return True
        else:
            s.add(item)
    return False

A = [5, 7, 1, 2, 8, 4, 3]
val = 10
t.assertTrue(find_sum_of_two(A, val))
val = 19
t.assertFalse(find_sum_of_two(A, val))

def find_sum_of_two1(A, val):
    '''
    O(N)
    use constant space
    '''
    min, max = 0, len(A) - 1
    while min < max:
        if A[min] + A[max] == val:
            return True
        elif A[min] + A[max] > val:
            max -= 1
        elif A[min] + A[max] < val:
            min += 1
    return False 



A = [5, 7, 1, 2, 8, 4, 3]
val = 10
t.assertTrue(find_sum_of_two1(A, val))
val = 19
t.assertFalse(find_sum_of_two1(A, val))
