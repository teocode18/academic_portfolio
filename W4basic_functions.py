#Q1
def filter_positive_numbers(numbers):
    """
    Filters out positive numbers from the list, keeping only the negative ones.
    The function returns a list of all the positive numbers in the input.
    
    Args:
        numbers (list of int): A list of integers.
    
    Returns:
        list of int: A list containing only the positive integers.
    """
    return [num for num in numbers if num > 0] 

list =[-3 , -6, 9, 12, 18, -22, 97, 64, 77]
result=filter_positive_numbers(list)
print(result)



#Q2
def valid_temperature(temperature):
     if temperature >= -100 and temperature <= 100:
         return True
     else:
         return False
     
def celsius_to_fahrenheit(celsius):
     fahrenheit = (celsius * 9/5) + 32
     return fahrenheit
 
 ''' Given the two functions and the following code to get the temperature from the user,
  complete the rest of the program to use these functions to print the temperature in Fahrenheit
  if the temperature from the user is within the range, otherwise print "Invalid temperature. Please enter a value between -100 and 100" '''
 
celsius = float(input("Enter temperature in Celsius: "))

if valid_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"The temperature in Fahrenheit is: {fahrenheit}")
else:
    print("Invalid temperature. Please enter a value between -100 and 100.")
