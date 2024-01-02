print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
if height>120: # If Height is greater than 120cm
    print("You can ride the rollercoaster.")
    age=int(input("What is your age? "))
    if age<=18: #If age is less than or equal to 18 years
        print("Please pay $7.")
    else:
        print("please pay $12.")
else:
    print("You can't ride the rollercoaster.")