# Reference 1: https://www.youtube.com/watch?v=7LKy3lrkTRA
# Reference 2: https://en.wikipedia.org/wiki/Farey_sequence
# Reference 3: https://mathworld.wolfram.com/FareySequence.html


import time # Using time module to calculate the speed of the algorithm execution in python
import math # Used for custom round function which cuts off at the closest non-zero digit after the decimal point


# Utility to seperate a string into its characters/digits
'''
    @param string - A string you want to split into its digits/characters
    @return [char for char in string] - A list of all the characters/digits in the @param string
    @return type - List
'''
def seperate(string):
    return [char for char in string]


# Custom round function which cuts off at the closest non-zero digit after the decimal point
'''
    @param number - A number you want to round to the first non-zero digit after the decimal point
    @return  value - The @param number but with only the first non-zero digit after the decimal point
    @return type - List
'''
def customRound(number):

    # If the number is 0 then it rounds to a 0 
    if number == 0:
        return 0

    # Gets the sign of the value
    sign = -1 if n < 0 else 1

    # Gets the scale of the number
    scale = int(-math.floor(math.log10(abs(number))))

    # If the scale less than or equal to 0 set the scale to 1
    if scale <= 0:
        scale = 1

    # Otherwise find the factor by getting the 10th index of the scale
    factor = 10**scale

    # Output of the rounding calculations
    value = sign*math.floor(abs(number)*factor)/factor
    return value


# Test the accuracy of the algorithm's estimation
'''
    @param actual_value - A number you want to find the closest estimated rational fraction possible to
    @param estimation - A rational fraction that is really close to the @param actual_value generated from Farey's Estimation Algorithm 
    @return  matching_accuracy - The accuracy that @param estimation is to @param actual_value
    @return type - float
'''
def accuracyOfAlgorithm(actual_value, estimation):
    
    # Get digits that the actual value and estimation value have
    digits_actual_value = seperate(str(actual_value))
    digits_estimation = seperate(str(estimation))

    # We require anything after the decimal point to measure the algorithm's accuracy 
    after_decimal_point_actual_value = digits_actual_value[2:]
    after_decimal_point_estimation = digits_estimation[2:]

    
    matches = 0 # Amount of digits matched in both numbers
    digits_used = 0 # Amount of digits compared in the loop

    # Loop to compare each digit in parallel from each list of digits (from actual value & estimation
    for digit_x, digit_y in zip(after_decimal_point_actual_value, after_decimal_point_estimation):

        # Add 1 to digits used counter to we can track how many digits we have compared in the parallel comparison
        digits_used += 1
        
        # Comparison between each digits in parallel
        if  digit_x == digit_y:

            # If matched digit is detected then add 1 to the match counter
            matches += 1

    # Calculate the accuracy of the algorithm 
    matching_accuracy = matches / digits_used * 100
    return matching_accuracy


# Function to execute the Farey Algorithm
'''
    @param value - A number you want to find the closest estimated rational fraction possible to
    @param limit - The limit you want the Farey's Estimation Algorithm to calculate to
    @return  numerator, denominator - Returns the closest rational fraction to the @param value as a tuple
    @return type - tuple
'''
def fareyAlgorithm(value, limit):

    # Limits less than 1 usually generate a ZeroDivisionError in the accuracy function therefore, 
    # we check if anyone does try to use a lower limit than 1 it will throw them an error
    if limit < 1:
        raise ValueError('The order of the approximation must be larger than 1')
    
    # If user enters value less than 0, then we make the numerator negative
    if value < 0:
        numerator, denominator = fareyAlgorithm(-value, limit)
        return -numerator, denominator

    # Subtract the limit from itself to the lowest value which should be 0, 
    # as this is the lower bound for the Farey Algorithm
    z = limit - limit

    # Get the upper & lower limits of the mediant
    lower, upper = (z, z+1), (z+1, z)

      
    # Create a while loop in order to loop the calculation until we reach a value
    while True:

        # Get the mediant value of each iteration
        mediant = (lower[0] + upper[0]), (lower[1] + upper[1])

        '''
            @var mediant[0] - The numerator of the most accurate fraction
            @var type - float
            
            @var mediant[1] - The denominator of the most accurate fraction
            @var type - float            

        '''
        
        # Check if the value given multiplied by the highest denominator is greater than the numerator
        if value * mediant[1] > mediant[0]:

            # If the limit given is bigger than the denominator then end the loop and return the upper value
            if limit < mediant[1]:
                return upper

            # Otherwise return the lower value as the mediant
            lower = mediant

        # Check if the value given multiplied by the highest denominator is equal to the numerator
        elif value * mediant[1] == mediant[0]:

            # If limit is greater than or equal to the denominator then we return the mediant
            if limit >= mediant[1]:
                return mediant

            
            # Otherwise if the denominator of the lower bound is greater than the denominator of the upper bound return the lower bound fraction
            if lower[1] < upper[1]:
                return lower

            # Otherwise return the upper bound fraction
            return upper


        # Any other cases
        else:
            
            # If the limit is smaller than the denominator then we return the lower bound fraction
            if limit < mediant[1]:
                return lower

            # Otherwise equate the upper bound fraction the the mediant
            upper = mediant


# Main logic to test the Algorithm       
print()

value = float(input('Enter a value you would like to estimate: '))
order = int(input('The order of the approximation: '))

print()
print('Running Farey Algorithm on value {} to an order of {}...'.format(value, order))
print()

start = time.time()
numerator, denominator = fareyAlgorithm(value, order)
end = time.time()

print()
print('Found a rational fraction of {}/{}'.format(int(numerator), int(denominator)))
print()

algo_accuracy = accuracyOfAlgorithm(value, numerator / denominator)
print('Matching accuracy of {}%'.format(algo_accuracy))
print()

total_time = customRound(end - start) 
print('Computational Time: {} seconds'.format(total_time))



