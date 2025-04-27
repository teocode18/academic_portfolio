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
