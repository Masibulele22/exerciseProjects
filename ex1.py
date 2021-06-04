#Hundredth Birthday Year:
#For this execrcise I had to create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#I imported date object from the python datetime library. 
#Used the built-in python method "today" to get the current date and gave it a variable instance
#From that variable instance I accessed the "year" property and gave it also a variable instance called "this_year" 
from datetime import date
todays_date = date.today()
this_year = todays_date.year

#For the user's username I got a string variable input
#For the ser's age I got an integer variable input 
user_name = str(input("Please enter your name: "))
user_age = int(input("Please enter your age: "))

#I minused the user's current age from 100 to get his years left until he/she reaches 100 years and named it as an instance of "years_left"
years_left = 100 - user_age

#I then added the user's years left until 100 to this year to get the user's 100th birthday year
user_hundredth_birthday_year = this_year + years_left 

#I then printed the personalized message by concatenating user's username and 100th birthday year with the message as string variables
print(str(user_name) + ", you will be 100-years-old in the year " + str(user_hundredth_birthday_year))
