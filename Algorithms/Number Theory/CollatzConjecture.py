# Reference: https://en.wikipedia.org/wiki/Collatz_conjecture

import time, random  # Import the modules that are going to be used

results = []  # List of numbers from the collatz's conjecture


def collatzConjecture(number):  # Define the function of collatz's conjecture
    if number % 2 == 0:  # Check the number is an even
        return number // 2  # Return the floor divison of the value by 2

    elif number % 2 == 1:  # Check the number is an odd
        result = 3 * number + 1  # Do the collatz's conjecture odd function
        results.append(result)  # Append results to a list of results
        
        return result  # Return the result


# A huge random integer
random_int = random.randint(1, 99999)
print("Using value {} for Collatz's Conjecture".format(random_int))  # Print what value the function will use

digits = len(str(n))  # Amount of digits in the number

start = time.time()  # Start time of function

while random_int != 1:  # While the conjecture doesn't return 1
    random_int = collatzConjecture(int(random_int))  # Run the conjecture function

end = time.time()  # End time when the while loop is finished

tt = end - start  # Calculate time taken

print('')
print('Time Taken: ', tt, 's')  # Print time taken
print('Digits: ', digits)  # Amount of digits in the initial starting value
print('Digits per second: ', digits / tt, ' dps')  # Digits calculated per second
print('Seconds per digit: ', tt / digits, ' spd')  # Seconds per digit, to see how fast a digit is caluclated
print('Size of results list: ', len(results))  # Amount of numbers in the results list
