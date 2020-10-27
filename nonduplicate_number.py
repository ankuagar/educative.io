#!/usr/bin/env python3
import unittest
t = unittest.TestCase()
def nonDuplicateNumber(lst):
    '''
    Uses xor operation to filter the unique number
    '''
    ans = 0
    for num in lst:
        ans ^= num
    return ans 

t.assertEqual(1, nonDuplicateNumber([4, 3, 2, 4, 1, 3, 2]))
t.assertEqual(1, nonDuplicateNumber([2,2,1]))
t.assertEqual(4, nonDuplicateNumber([4,1,2,1,2]))
t.assertEqual(1, nonDuplicateNumber([1]))
t.assertEqual(0, nonDuplicateNumber([0]))
