# Reference 1: https://mathschallenge.net/library/number/number_of_divisors#:~:text=We%20begin%20by%20writing%20the,p%20a%20)%3D%20a%20%2B1.
# Reference 2: https://en.wikipedia.org/wiki/Divisor_function
# Euler's Paper: https://scholarlycommons.pacific.edu/euler-works/175/

# We can model this problem into an equation
# Where n is the number we want to find the amount of divisors from
# and where d(n) is the amount of diviors value n has

# Math Proof:
# n can be modelled as (p ^ a)(q ^ b)(r ^ c)(s ^ d)
# which means we can prime factor decompose value n into
# its prime factor decomposed form
# therefore meaning that d(n) = (a+1)(b+1)(c+1)(d+1)
# which gives us the correct amount of divisors value n has
#
# If the prime factorization of n is Fig 1 (https://gyazo.com/275dddc80deafb0c4106ff654e41a11a)
# where Pk are the distinct prime factors and ak are the positive integer exponents, then
# the sum of all the positive integer factors is d(n) Fig 2 (https://gyazo.com/2c080c9a6a8230679fd88eb17018daff)
# general form of the summation Fig 3 (https://gyazo.com/9f795cec3a1f7717eeefcce9232ad379)

from math import sqrt

#
# @param num - Number you wish to get the amount of divisors of
# @return divisors - The amount of divisors @param num has
#
def noOfDivisors(num):
    #
    # A method to decompose the @param num into its prime factors
    #
    prime_factors_list = []
    while num % 2 == 0:
        prime_factors_list.append(2)
        num /= 2

    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            prime_factors_list.append(i)
            num /= i

    if num > 2:
        prime_factors_list.append(int(num))

    #
    # Formula:
    # n = (p ^ a)(q ^ b)(r ^ c)(s ^ d)
    # Get the index of each prime factor from the prime factor decomposition of @param num
    #
    index_of_two = prime_factors_list.count(2)
    index_of_three = prime_factors_list.count(3)
    index_of_five = prime_factors_list.count(5)
    index_of_seven = prime_factors_list.count(7)

    #
    # Formula:
    # d(n) = (a+1)(b+1)(c+1)(d+1)
    # return divisors - Amount of divisors the number @param num has aka output of d(n)
    #
    divisors = (index_of_two + 1) * (index_of_three + 1) * (index_of_five + 1) * (index_of_seven + 1)
    return divisors


value = int(input('Value: '))
divisors = noOfDivisors(value)
print(divisors)
