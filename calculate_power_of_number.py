#!/usr/bin/env python3
import unittest
import time
t = unittest.TestCase()
def power(x, n):
    '''
    O(N) solution, time and memory (on the stack)
    '''
    if n == 0:
        return 1
    elif x == 1:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return 1/x * power(1/x , -1*n-1)
    else:
        return x * power(x, n-1)

t.assertEqual(1, power(0,0))
t.assertEqual(32, power(2,5))
t.assertEqual(81, power(3,4))
t.assertEqual(3.375, power(1.5,3))
t.assertEqual(.25, power(2,-2))
t.assertEqual(.125, power(2,-3))


memory_map = {}
def power1(x, n):
    '''
    Uses memoization to store duplicate results.
    '''
    if n == 0:
        return 1
    elif x == 1:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return 1/x * power1(1/x , -1*n-1)
    elif (x,n) in memory_map:
        return memory_map[(x,n)]
    else:
        val = power1(x, n//2) * power1(x, n-n//2)
        memory_map[(x,n)] = val
        return val

t.assertEqual(1, power1(0,0))
t.assertEqual(32, power1(2,5))
t.assertEqual(81, power1(3,4))
t.assertEqual(3.375, power1(1.5,3))
t.assertEqual(.25, power1(2,-2))
t.assertEqual(.125, power1(2,-3))



def power2(x,n):
    '''
    Does not use memoization
    O(logn) time (function calls) and memory (on stack)
    If n is even result is temp * temp where temp is x ** n//2
    If n is odd result is temp * temp * x where temp is x ** n//2
    For negative n, inverse the final result. For intermediate steps 
    keep n positive by multiplying by -1
    '''
    if n == 0:
        return 1
    elif x == 1:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        temp = power2(x, -1*n//2)
    else:
        temp = power2(x, n//2)    
    if n % 2 == 0:
        result =  temp * temp
    else:
        result = x * temp * temp 
    
    if n < 0:
        return 1/result
    else:
        return result

t.assertEqual(1, power2(0,0))
t.assertEqual(32, power2(2,5))
t.assertEqual(81, power2(3,4))
t.assertEqual(3.375, power2(1.5,3))
t.assertEqual(.25, power2(2,-2))
t.assertEqual(.125, power2(2,-3))
now = time.time()
power2(2,100) # intermediate, doubles the computation on half the exponent
print(time.time() - now)
now = time.time()
power1(2,100) # fastest, uses memoization
print(time.time() - now)
now = time.time()
power(2,100) # slowest, multiplies n times
print(time.time() - now)