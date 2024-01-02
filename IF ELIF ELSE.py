print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
if height>120:
    print("You can ride the rollercoaster.")
    age=int(input("What is your age? "))
    if age<12:
        print("Please pay $5.")
    elif age<=18:
        print("Please pay $7.")
    elif age<=22:
        print("Please pay $10.")
    else:
        print("please pay $12.")
else:
    print("You can't ride the rollercoaster.")