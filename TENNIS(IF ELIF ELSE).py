print("Welcome to Tennis coaching centre")
age=int(input("Enter your age in years: "))
if age<6:
    print("They are eligible to play under the category of Beginner level")
elif age<10:
    print("They are eligible to play under the category of Intermediate Level")
elif age<14:
    print("They are eligible to play under the category of Senior Level")
else:
    print("They are eligible to play under the category of Pro Level")