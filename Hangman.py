# Step-1
import art
import WORDS
word_list= word_list.WORDS()
#1-Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
#1:Create a variable called 'lives' to keep track of the number of lives to keep track of the number of lives left
# Set lives to equal 6
end_of_game=False
lives=6

#Code:
print(f"Pssst, the solution is {chosen_word}")
display=[]
word_length=len(chosen_word)
for _ in range(len(chosen_word)): # Create Blanks
    display +="_"
print(display)
#2-Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
end_of_game=False # It is denoted to be the end of game when display has no blanks

while not end_of_game:
    Guess=input("Guess a letter: ").lower()

 #3-Check if the letter the user guessed (Guess) is one of the letters in the chosen_word
for position in range((word_length)):
    letter=chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {Guess}")
    if letter==Guess:   
        display[position]=letter
 
 #2: If the guess is not a letter in the chosen_word, reduce the lives by 1
if Guess not in chosen_word:
    print(f"You guessed{Guess}, that is not in a word, you lose a life")
    lives-=1 # Reduces the lives by 1
    if lives ==0:
        end_of_game=True
        print("You lose")



#Step-2 and 3
#1-Create an empty list called display.
# For each letter in chosen_word, add a "_" to 'display'.
#Ex: If the chosen word was "apple", display should be ["_","_","_","_","_","_","_","_","_"], representing each letter to guess
#2- If the letter at the position matches 'guess' then reveal that letter in the display of that position.
#Example: If the user guesses 'p', and the first letter of apple is 'p', display would become ["_""p"e"_"_"]
#3- Print 'display and you should see the guessed letter in the correct position and every other letter replaced with "_".
print(f"{''.join(display)}")

if "_" not in display:  #In: it basically allows us to see if a particular element exists inside a list
    end_of_game="True"
    print("You win!")


#Step-4
#1:Create a variable called 'lives' to keep track of the number of lives to keep track of the number of lives left
# Set lives to equal 6
    #2: If the guess is not a letter in the chosen_word, reduce the lives by 1
    #3: Print the ASCII art from stages that corresponds to the remaining lives the user has remaining]
