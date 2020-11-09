from math import log

'''
    @function left_shift - Finds all the variables within a left bit shift operation

    Operation must have the form:
        k << n = y

'''
def left_shift(k=None, n=None, y=None):
    
    '''
        @param k - The value of the right side ("prefix") of the bitwise operation
        @param n - The value of the left side of the bitwise operation
        @param y - The output of the bitwise operation           
    '''

    '''
        @const l - The constant found in both shift equations to find the @param n 
    '''
    l = log(2)

    # If k is not given find the value of k 
    if k is None:
        k = y / (2 ** n)
        return k

    # If n is not given find the value of n
    elif n is None:
        n = log(y/k) / l
        return n

    # If y is not given find the value of y
    elif y is None:
        y = k * (2 ** n)
        return y

'''
    @function right_shift - Finds all the variables within a right bit shift operation

    Operation must have the form:
        k >> n = y

'''
def right_shift(k=None, n=None, y=None):
    
    '''
        @param k - The value of the right side ("prefix") of the bitwise operation
        @param n - The value of the left side of the bitwise operation
        @param y - The output of the bitwise operation           
    '''

    '''
        @const l - The constant found in both shift equations to find the @param n 
    '''
    l = log(2)

    # If k is not given find the value of k 
    if k is None:
        k = y * (2 ** n)
        return k

    # If n is not given find the value of n
    elif n is None:
        n = log(k/y) / l
        return n

    # If y is not given find the value of y
    elif y is None:
        y = k / (2 ** n)
        return y

