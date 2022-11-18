"""
full adder
"""
from OR_gate import OR
from half_adder import half_adder


def full_adder(a, b, c):  # output (carry, sum)

    # first half_adder
    ha1 = half_adder(a, b)
    ha1_sum = ha1[1]
    ha1_carry = ha1[0]

    # second half_adder two
    ha2 = half_adder(ha1_sum, c)
    ha2_sum = ha2[1]  # also full_adder sum
    ha2_carry = ha2[0]

    # or gate, third step, carry value
    ha_or = OR(ha1_carry, ha2_carry)

    carry = ha_or
    fa_sum = ha2_sum

    return carry, fa_sum
