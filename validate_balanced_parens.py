#!/usr/bin/env python3
import unittest
t = unittest.TestCase()
def balanced_parens(s):
    '''
    Test if the input string contains balanced parentheses
    Examples:
        Input: "((()))"
        Output: True
        Input: "])}"
        Output: False
    Args:
        String s: The input string, containing only chars '(', '{', '[', ')', '}', ']'
    Returns:
        Boolean True or False: True if input string contains balanced chars
    '''
    paren_pairs = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }
    stack = []
    for elem in s:
        if elem in {'(', '{', '['}:
            stack.append(elem)
        elif len(stack) != 0 and paren_pairs[elem] == stack.pop():
            pass
        else:
            return False
    
    return len(stack) == 0

def test_balanced_parens():
    t.assertTrue( balanced_parens("((()))") )
    t.assertTrue( balanced_parens("[()]{}") )
    t.assertTrue( balanced_parens("[({})]") )
    t.assertFalse( balanced_parens("({[)]") )
    t.assertFalse( balanced_parens("(") )
    t.assertFalse( balanced_parens("])}") )

test_balanced_parens()