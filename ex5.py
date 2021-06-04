#Number Checker:
#In this exercise I had to write a Python program to check if a user input number is positive, negative, or zero.

#Instantiated an input variable that takes in a float.
inputNumber = float(input("Please enter your number here: "))

#I created conditional statements to determine if the input variable is negative, zero or positive
#by creating a condition if the input is greater than, less than or equal to zero. 
if(inputNumber < 0):
    print("The input number is a negative number.")
elif(inputNumber == 0):
    print("The input number is zero.")
elif(inputNumber > 0):
    print("The input number is a positive number.")
else:
    print("Please enter a valid number!")

