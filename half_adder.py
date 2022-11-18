"""
half adder

"""
from XOR_gate import XOR
from AND_gate import AND


def half_adder(x, y):
    # returns a tuple (1, 0) etc. (carry, sum)
    carry = AND(x, y)
    sum_of = XOR(x, y)
    return carry, sum_of
