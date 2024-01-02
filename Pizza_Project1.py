print("Thank you for choosing Python Pizza Deliveries!")
Size=input("What Size pizza Do you want?'S','M','L'")
add_pepporoni=input("Does the user want pepporoni?'Y' or 'N'")
extra_cheese=input("Does the user wants extra cheese?'Y' or 'N'")
bill=0 #Set bill=0
if Size=='S':
    bill +=15
elif Size=='M':
    bill +=20
elif Size=='L':
    bill +=25

if add_pepporoni=='Y':
    bill +=2
else:
    bill +=3

if extra_cheese=="Y":
    bill+=1
else:
    print(f"Your final bill is {bill}")