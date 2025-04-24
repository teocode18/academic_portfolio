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
