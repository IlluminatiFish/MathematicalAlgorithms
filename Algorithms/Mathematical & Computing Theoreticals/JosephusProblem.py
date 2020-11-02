# Reference: https://www.youtube.com/watch?v=uCsD3ZGzMgE

# We can model the Josephus Problem into an equation
# Where n is the amount of soldiers in the problem and
# Where W(n) is the winning seat that does not get killed

# Assumption:
# W(n) value is based on the assumption
# that the solider of n value 1 always starts

# Math Proof:
# If n = 2^a + l
# Where l < 2^a
# Then W(n) = 2l + 1

from math import log, floor, trunc

soldiers = int(input('[+] Soldiers: '))

#
# @param value - The value you want to decompose
# @param factor - The factor we want to decompose the @param value by
# @function powerFactorDecomposition(@param value, @param factor) -
# Gets the closest number to @param value when @param value is decomposed
# into index factors of @param factor

# Instead of using python's built-in method of ceil() (which
# rounds to the next value), as the second value of the tuple,
# I used math.trunc() as it terminates anything after the decimal
# and works much better than ceil(), also fixes the fact n = 7
# returned a value of -1 for W(n).

def powerFactorDecomposition(value, factor):
    val = floor(log(value, factor)), trunc(log(value, factor))
    closest_power = min(val, key=lambda z: abs(value-factor**z))
    return factor ** closest_power

#Closest power of @param factor to the @param value passed
factor_decompose = powerFactorDecomposition(soldiers, 2)

left_over = soldiers - factor_decompose

# Then W(n) = 2l + 1
winning_seat = (2 * left_over) + 1
print('[=] The survivor of the Josephus Problem is the soldier sitting in position {}'.format(winning_seat))
