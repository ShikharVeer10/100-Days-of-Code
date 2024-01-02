print("Welcome to the Treasure Island. Your mission is to find the treasure")
choice_1=input("You are at the middle of the crossroads. Which way do you want to go? Left or Right?")
if choice_1=="Right":
    print("Game over")
else:
    swimming=input("Do you want to swim or wait?")
    if swimming=="wait":
        print("Which door?")
    else:
        Door=input("Which door do you want to go Red or blue or yellow")
        if Door=="Yellow":
            print("You win")
        else:
            print("You Lose")
        

        

            
               
            
