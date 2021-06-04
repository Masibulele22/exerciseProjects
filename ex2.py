#Username And Password:
#For this exercise I had to Create a program that requests a username and password. 
#The program will greet the user by name before checking whether the password matches the string “LearningPythonIsFun”. 
#If the condition is True, print out “Access Granted” otherwise it will print out “Access Denied”.

#I instantiated my password as a variable
password_condition = "LearningPythonIsFun"

#Instantiated a variable to take in a string input for the user's username
#Concatenated the variable as a string to the print-out greeting message 
user_name = str(input("Please enter your username: "))
print("Oh hello there "+ str(user_name) + "!")

#Instantiated a variable for the user's password as an input string 
user_password = str(input("Please enter your password: "))

#Made a condition where if the user's input variable matches the instantiated variable password then it would print "Access Granted".
#If not then it would print "Access Denied"
if(user_password == password_condition):
    print("Access Granted")
else:
    print("Access Denied")

