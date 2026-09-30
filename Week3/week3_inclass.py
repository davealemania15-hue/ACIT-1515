micheal = 17

legal_age = 19

if micheal >= legal_age:
    print("You can drink alcohol.")

username = "micheal"
password = "123"
min_length = 10

if len(password) >= min_length:
    print("you registered succuessfully.")
else:
    print("Password must be at least 10 characters long.")

# Figure out if a number is odd or even
# use input() to get a number from the user
# if the user input is not a number, print "Please enter a valid number."
# if the number is even, print "The number is even."

#This is my answer to the question above
num = input("Enter a number: ")
num = int(num)

if num != int(num):
    print("Please enter a valid number.")
else:
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is not even.")

if num % 2 == 0:
    print("The number is even.")
    else:
        print("The number is odd.")

#Teacher's answer to the question above
number = input("Enter a number: ")
number = int(number)

if user_input.numeric():
    if number % 2 == 0:
    
        print("The number is even.")
    else:
        print("The number is not even.")
else:
    print("You did give us a number.")

use_input2 = input("Enter a number: ")

#this is what a function looks like 
#def = name the variable, then put () after it, then put : after the ()

def odd_or_even():
    if use_input2.isnumeric():
        number = int(use_input2)
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    else:
        print("You didn't give us a number.")

#test run the function
user_input = input("Enter a number: ")
odd_or_even(user_input)

#You can hide the code by CRTL + /

def times_by_ten(n):
    print(n * 10)

times_by_ten(4)
times_by_ten(3)

def odd_or_even(n):
    if n % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


odd_or_even(times_by_ten(4)) #THIS IS WHERE WE TURN THE MACHINE ON AND RUN THE FUNCTION

returnedValue = times_by_ten(4)
print(returnedValue) #this will print None because the function does not return anything

#and

print(times_by_ten(4)) #this will also print None because the function does not return anything

numbers = [1, 2, 3, 4, 5] #This is what we call a list in python. It is a collection of values that are stored in a single variable.

#more examples

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])  # This will print "apple"\

numbers = [1, 2, 3, 4, 5]
print(numbers[3])  # This will print "4" because the index starts at 0.

def odd_or_even(user_input):

#instead of writing 500 times of print index, you can for loop through the list and print each index.
for number in numbers:
odd_or_even(number)

# For (could be any nickname) IN (the name of the list you want to loop through):