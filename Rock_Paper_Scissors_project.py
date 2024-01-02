import random

user_choice=int(input("What do you choose?Type 0 for rock,1 for paper,2 for scissors")) #Since the character > supports only int data type we need to mention the function int
computer_choice=random.randint(0,2)
print(f"Computer Chose {computer_choice}")

if user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice>user_choice:
    print("You lose")
elif computer_choice>user_choice:
    print("Computer wins")
elif user_choice>computer_choice:
    print("user wins")
elif user_choice>computer_choice:
    print("Computer loses")
elif computer_choice==user_choice:
    print("It is a draw")
elif user_choice>=3 or user_choice<0:
    print("You typed an invalid number! please type any number between 0,1 and 2")