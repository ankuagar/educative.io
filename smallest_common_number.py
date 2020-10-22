#!/usr/bin/env python3
import unittest
t = unittest.TestCase()
def find_least_common_number(a, b, c):
    '''
    Find the smallest common number among given three sorted lists
    Args:
        a: integer list 1
        b: integer list 2
        c: integer list 3
    Returns:
        int: smallest number among the three sorted lists or -1
    Example:
        find_least_common_number([6,7,10,25,30,63,64], [0,4,5,6,7,8,50], [1,6,10,14]))
        should return 6        
    '''
    i=j=k=0
    lena, lenb, lenc = len(a), len(b), len(c)
    while i < lena and j < lenb and k < lenc:
        if a[i] == b[j] == c[k]:
            return a[i]
        elif a[i] == min(a[i], b[j], c[k]):
            i+=1
        elif b[j] == min(a[i], b[j], c[k]):
            j+=1     
        elif c[k] == min(a[i], b[j], c[k]):
            k+=1
        else:
            pass # control should not reach here

    return -1

t.assertEqual(6, find_least_common_number([6,7,10,25,30,63,64], [0,4,5,6,7,8,50], [1,6,10,14]))
t.assertEqual(6, find_least_common_number([6], [6], [6]))
t.assertEqual(-1, find_least_common_number([6,7,10,25,30,63,64], [0,4,5], [100,600,1000,1400]))
t.assertEqual(-1, find_least_common_number([6,7], [0,1], [100, 200]))
t.assertEqual(-1, find_least_common_number([6], [0], [100]))