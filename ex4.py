# Guess The Missing Letter:
# For this exercise I had to choose a random word and choose a random letter within that word that you'll represent with a _.
# The program will ask the user to guess the missing letter.
# The program lets the user know whether the guess was correct or not.

# I imported the 'random' module and used the 'choice'method to generate a random from my list of words
# I also used the 'choice' method to get a random letter from my random word that I already instantiated as its own variable  
import random

listOfWords = ['ambivert', 'deafness', 'entrance', 'glued', 'kingdom', 'climbed', 'outdoors', 'great', 'losing', 'loud', 'themselves', 'things', 'pistols',
                     'redbugs', 'sleeps', 'cool', 'megacity', 'eleven', 'snakes', 'subrules', 'subtrends', 'torrents', 'unhides', 'town', 'supper', 'suplex', 'reflex', 'steep', 'stumps']

random_word_from_list = random.choice(listOfWords)
random_letter = random.choice(random_word_from_list)

# I used the 'random_word_from_list' variable and replace method to replace the random letter with a one spaced underscore 
missing_letter_word = random_word_from_list.replace(random_letter, '_', 1)

#I made an input string prompt to get the user's name input and saved it to a string variable called "username"
#I printed the username variable as a string that is concatenated to the output greeting
username = str(input("Input name : "))
print("Hi "+str(username)+" ! Let's play hangman...")

#I concatenated the missing letter variable as a string and typed this inside an input prompt to get the user's input to guess the missing letter  
missing_letter_guess = str(input("Guess the missing letter in " + "'" + str(missing_letter_word)+ "'" + " : "))

#I made a conditional statement where the missing letter guess from the user must match the missing random letter in the random word
# Else if user's missing letter guess does not match the random letter from the random word it will print incorrect 
if(str(missing_letter_guess) == str(random_letter)):
    print("Good guess!")
    print("The word was: " + str(random_word_from_list))
else:
    print("Incorrect!")
    print("The word was: " + str(random_word_from_list))

