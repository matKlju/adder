"""
8-bit ripple carry adder
"""
from random import choice as rnd
from full_adder import full_adder
from half_adder import half_adder


def eight_bit_adder(a0, a1, a2, a3, a4, a5, a6, a7,
                    b0, b1, b2, b3, b4, b5, b6, b7: int) -> tuple:

    adder_sum = []

    ab = [a0, a1, a2, a3, a4, a5, a6, a7]
    ac = [b0, b1, b2, b3, b4, b5, b6, b7]

    # first adding
    ha = half_adder(a0, b0)
    ha_carry = ha[0]
    ha_sum = ha[1]
    adder_sum.append(ha_sum)

    # next 7 adding
    fa_carry = 0
    for i in ab[1: 8]:
        for y in ac[1: 8]:
            fa = full_adder(ha_carry, i, y)  # fa = (carry, sum)
            fa_carry = fa[0]  # fa_carry = carry
            fa_sum = fa[1]  # fa_sum = sum
            adder_sum.append(fa_sum)
            break

        ha_carry = fa_carry

    # Overflow flag
    if ha_carry == 1:
        overflow = True
    else:
        overflow = False

    adder_sum.reverse()
    return adder_sum, overflow


print(eight_bit_adder(1, 1, 1, 1, 1, 1, 1, 0,
                      1, 1, 1, 1, 1, 1, 1, 1))
