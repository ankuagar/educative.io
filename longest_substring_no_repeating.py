#!/usr/bin/env python3
import unittest
t = unittest.TestCase()
def longest_non_repeating_substring(s):
    max_seq_length = temp_max_seq_length = 0
    max_start_idx = max_end_idx = temp_max_start_idx = None
    coll = set()
    for idx, elem in enumerate(s):
        if elem not in coll:
            temp_max_seq_length += 1
            coll.add(elem)
            if temp_max_start_idx is None:
                temp_max_start_idx = idx 
        else:
            if temp_max_seq_length > max_seq_length:
                max_seq_length = temp_max_seq_length
                max_start_idx = temp_max_start_idx
                max_end_idx = idx - 1
            else:
                pass # if <= do nothing 
            temp_max_start_idx = idx # store current idx as start for next sub seq
            temp_max_seq_length = 1 # reset temp length to 1 to include current elem in next subseq 
            coll.clear() # clear coll and add current elem, as next sub seq starts from this one
            coll.add(elem)
    
    # check one last time after the str has exhausted, perhaps the longest seq is at the end of 
    # the input string
    if temp_max_seq_length > max_seq_length:
        max_seq_length = temp_max_seq_length
        max_start_idx = temp_max_start_idx
        max_end_idx = idx
    
    return max_start_idx, max_end_idx, max_seq_length
            
t.assertEqual(longest_non_repeating_substring('abrkaabcdefghijjxxx'), (5,14,10))
t.assertEqual(longest_non_repeating_substring('a'), (0,0,1))
t.assertEqual(longest_non_repeating_substring('aa'), (0,0,1))
t.assertEqual(longest_non_repeating_substring('aaaaaaaaaaa'), (0,0,1))
t.assertEqual(longest_non_repeating_substring('aab'), (1,2,2))
t.assertEqual(longest_non_repeating_substring(''), (None,None ,0))
t.assertEqual(longest_non_repeating_substring('aaaaaaaaaaab'), (10,11,2))
t.assertEqual(longest_non_repeating_substring('aaaaaaaaaaabaaabcccccc'), (14,16,3))
