'''syntax errors in Q1 - Q4 '''


#Q1
employees = {"joan": 32, "john", 41, "jane": 28}

for name,age in employees.items():
    print(f"{name.capitalize()} is {age} years old.")

#this is a dictionary employees after "john" its missing " : " on line 2


#Q2
numbers = [3, 8, -4, 22, 0]

for num in numbers
    num = num+1

print( numbers )

#there is a missing " : " at the end of line 4


#Q3
date = ( '2nd', 'February' )
date.append('2024')
print( date )
date2 = ('2nd', 'February', '2024')
print (date2)

#Tuples are unmutable, meaning that we cannot change, add or remove items after the tuple has been created.


#Q4
def add_one( number ) :
    '''add one to the number that is passed in'''
    return( number+ one )

print(add_one(5))

#here we get an error because "one" is not part of the argument, thia would only work if instead of "one" we replace it with 1 and the answer then would be 6


''' runtime errors Q5 '''
#Q5
numbers = [ 34, -2 , 4, 5 ]

for k in range(5) :
    print( numbers[k] )

#the error here is that instead of printing numbers 34, -2 , 4, 5 what happens is that we get an index error
#numbers = [ 34, -2 , 4, 5 ]

#for k in range(1) :
#    print( numbers )
# output becomes [ 34, -2 , 4, 5 ]



'''Using Assert '''

''' 
FizzBuzz is a simple number game.
You count from 1 and call out the number, except:
* if the number divides by 3 you say 'buzz'
* if the number divides by 5 you say 'fizz'
* if the number divides by both 3 and 5 you say 'fizzbuzz'

Verify that the implementation below is a correct implementation of the game
* Create simple tests of the values the function returns using assert
* Test boundary cases to ensure correct behaviour
* Verify that the sequence is correct for numbers up to and including 40
'''

def fizzbuzz(number):
    if number % 15 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'buzz'
    elif number % 5 == 0:
        return 'fizz'
    else:
        return number

# Basic tests
assert fizzbuzz(3) == 'buzz'
assert fizzbuzz(5) == 'fizz'
assert fizzbuzz(15) == 'fizzbuzz'
assert fizzbuzz(4) == 4
assert fizzbuzz(30) == 'fizzbuzz'
assert fizzbuzz(9) == 'buzz'
assert fizzbuzz(10) == 'fizz'
assert fizzbuzz(13) == 13

# Test numbers 1 to 40
expected = [
    1, 2, 'buzz', 4, 'fizz', 'buzz', 7, 8, 'buzz', 'fizz',
    11, 'buzz', 13, 14, 'fizzbuzz', 16, 17, 'buzz', 19, 'fizz',
    'buzz', 22, 23, 'buzz', 'fizz', 26, 'buzz', 28, 29, 'fizzbuzz',
    31, 32, 'buzz', 34, 'fizz', 'buzz', 37, 38, 'buzz', 'fizz'
]

for i in range(1, 41):
    assert fizzbuzz(i) == expected[i - 1]

print("All tests passed.")

# add further assertions to check the behaviour
# when you are sure the code functions correctly test it for all numbers up to 40 with a loop





