#Sum Calculator:
#For this exercise I needed to calculate the sum of two given integers within the range of 0 to 9 and prints the answer to the terminal. 
#If the input values are not within this range the program prints an error message and terminate.
#If the sum is between 15 to 20 it should return 20.

#I instantiated the two input variables that will only take in integers and made an instantiation for the sum of both variables.
first_integer_input = int(input("Please enter your first integer: "))
second_integer_input = int(input("Please enter your second integer: "))
integer_input_sum = first_integer_input + second_integer_input

#I made a conditional statement where if either one of the input variables are greater than 0 and smaller than 9 that thier sum can be printed
#I also made a nested conditional statement where if the sum of both variables are greater than 15 and smaller 20, the sum of both variables should thus be equal to 20
#The sum total of both variables will be printed for the global scoped conditional statement and nested conditional statement 
#Or else if either one of the input variables are smaller than 0 or greater than 9 that it must print an error message 
if(first_integer_input >= 0 and first_integer_input <= 9 and second_integer_input >= 0 and second_integer_input <= 9):
    if(integer_input_sum >= 15 and integer_input_sum <= 20):
        integer_input_sum = 20
    print(integer_input_sum)
else:
    print("Error!")
