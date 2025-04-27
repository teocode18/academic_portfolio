#Q1
def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of odd numbers 
    and the number of even numbers in a list. 
       
    Args:
        lstIntegers (list): A list of integers.
    r
    Returns:
        list: A list containing [odd_count, even_count].
    """
    odd_list = []
    even_list = []

    for number in lstIntegers:
        if number % 2 == 0 :
             even_list.append(number)
        else:
            odd_list.append(number)

    return [len(odd_list), len(even_list)]

  
print(odd_even([1, 2, 3, 4, 5]))  # Output: [3, 2]



#Q2
# Write a function point_properties(x1,y1,x2,y2) that takes the coordinates of two points (𝑥1,𝑦1)
# and (𝑥2,𝑦2) and returns both the distance between the points and the coordinates of the midpoint.
# The formula to find mid point of x = (x1+x2)/2, y = (y1+y2)/2. Return the midpoint as a tuple.
# The formula to find the distance between the two point, distance = √((x2 – x1)² + (y2 – y1)²).
# You can use math.sqrt() to find the square root of a number.
# The function returns the two values in the order: distance, midpoint

import math

def point_properties(x1,y1,x2,y2):
    mid_x = (x1+x2)/2
    mid_y = (y1+y2)/2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance, (mid_x, mid_y)


# You can make an example call to the function with
dist, mid = point_properties(0, 0, 4, 3)    # dist=5.0, mid = (2.0, 1.5)


print(f"Distance: {dist}")  # Output: Distance: 5.0
print(f"Midpoint: {mid}")   # Output: Midpoint: (2.0, 1.5)
print(point_properties(0, 0, 4, 3))



#Q3
def divide_and_remainder(dividend, divisor):
    """
    This function performs integer division and returns both the quotient and the remainder.
    
    Args:
        dividend (int): The number to be divided.
        divisor (int): The number by which the dividend is divided.
    
    Returns:
        tuple: A tuple containing (quotient, remainder).
    """
    
    quotient =  dividend // divisor    # complete this 
    remainder =  dividend % divisor   # complete this 

   # Returning both quotient and remainder
    return (quotient, remainder)   # complete this  


quotient, remainder = divide_and_remainder(10, 3)
print(f"Quotient: {quotient}")   # Output: Quotient: 3
print(f"Remainder: {remainder}") # Output: Remainder: 1

# Directly print the returned tuple
print(divide_and_remainder(33, 3))  # Output: (11, 0)
