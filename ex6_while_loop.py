#While Loop Printer:
#In this exercise I had to write a short program that prints the numbers 1 to 10 using a while loop.

#I instantiated my initial variable.
printedNumber = 1

#Created a While Loop that increments my initial variable by adding 1 for every loop as long as my variable is under 11.
#I also added a conditional statement that breaks if it reaches or increments to 10 
while printedNumber < 11:
    print(printedNumber)
    if(printedNumber == 10):
        break
    printedNumber += 1 
