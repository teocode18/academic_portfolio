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




#Q5
def income_tax_calculator(annual_income):
    """
    This function calculates the tax amount for a given taxable annual income based on the UK tax rates and allowances.
    The tax is calculated progressively across tax bands, as per the following rates and allowances:

    Band               |  Taxable income   | Tax rate 
    Personal allowance | Up to 12,570      | 0% 
    Basic rate         | 12,571 to 50,270  | 20%
    Higher rate        | 50,271 to 125,140 | 40%
    Additional rate    | over 125,140      | 45%

    Key Details:
    Personal Allowance: The first £12,570 of taxable income is tax-free.
    Progressive Taxation: Income tax is applied progressively across bands. For example, an annual income of £25,000 would be taxed as follows:
    The first £12,570 at 0% (personal allowance).
    The remaining £12,430 (i.e., £25,000 - £12,570) at 20% (basic rate).

    Args:
        annual_income: float

    Returns:
        a float, representing the total calculated tax, rounded to one decimal point. You can use the round() function, e.g round(tax, 1)
        0.0 if annual_income is not a positive integer.
    """

    if not isinstance(annual_income, (int, float)) or annual_income <= 0:
        return 0.0

    tax = 0.0

    if annual_income <= 12570:
        return 0.0

    # Basic rate
    if annual_income > 12570:
        basic_band = min(annual_income, 50270) - 12570
        tax += basic_band * 0.20

    # Higher rate
    if annual_income > 50270:
        higher_band = min(annual_income, 125140) - 50270
        tax += higher_band * 0.40

    # Additional rate
    if annual_income > 125140:
        additional_band = annual_income - 125140
        tax += additional_band * 0.45

    return round(tax, 1)


print(income_tax_calculator(12000))     # 0.0
print(income_tax_calculator(14000))     # 286.0
print(income_tax_calculator(25000))     # 2486.0
print(income_tax_calculator(100000))    # 27432.0

