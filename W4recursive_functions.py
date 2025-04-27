#Q1
def countdown(number): 
    '''  
    This function takes a positive integer number  
    and prints the number down to zero. 
    ''' 
    if number < 0:
        return   # Base case: stop recursion when number is less than 0
    
    print(number)
    countdown(number - 1)



#Q2
def digits_sum(number):
    """
    This recursive function calculates the sum of digits of a given positive integer.
    """
    # Base case: if number is a single digit
    if number < 10:
        return number
    
    # Recursive case: split last digit and recurse on the rest
    return (number % 10) + digits_sum(number // 10)

# Testing
print(digits_sum(987))    # Output: 24
print(digits_sum(12345))  # Output: 15
print(digits_sum(24)) # output 6

#24 % 10 = 24-10 = 4
#24 // 10 = 2.4 round down = 2
#sum 4 + 2 = 6
