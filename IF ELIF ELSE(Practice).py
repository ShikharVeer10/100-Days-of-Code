print("Welcome to the fest!")
age=int(input("Enter your age in years?"))
if age<10:
    print("You are allowed to go the fest for free")
elif age<12:
    print("Please pay $5")
elif age<14:
    print("Please pay $7")
elif age<16:
    print("Please pay $9")
elif age<18:
    print("Please pay $50")
else:
     print("You cannot go for the fest")