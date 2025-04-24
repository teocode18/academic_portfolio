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




#Q3
"""
Basic Calculator Program

This program allows the user to perform basic arithmetic operations including
addition, subtraction, multiplication, and division. It prompts the user to
input two numbers and select an operation to perform. The program then
displays the result of the chosen calculation. """

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: cannot divide by zero"
    return num1 / num2


def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2


def get_operation():
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    return int(input("Enter your choice (1-4): "))


def calculate_result(num1, num2, operation):
    match operation:
        case 1:
            return addition(num1, num2)
        case 2:
            return subtraction(num1, num2)
        case 3:
            return multiplication(num1, num2)
        case 4:
            return division(num1, num2)
        case _:
            return "Undefined operation"


def run_program():
    num1, num2 = get_numbers()
    operation = get_operation()
    result = calculate_result(num1, num2, operation)
    print(f"Result: {result}")

