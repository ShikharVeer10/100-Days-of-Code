print("Welcome to the rollercoaster")
height=int(input("What is your height in cm?"))
bill=0 # The bill is set to 0 as its initial value

if height>120: #Only possible condition
  print("You can ride the rollercoaster")
age=int(input("What is your age?"))
if age<12:
    bill=5
    print("Child tickets are $5.")
elif age<=18:
    bill=7
    print("Child tickets are $7.")
else:
    bill=3
    print("Adult tickets are $12")
Photos=input("Do you want to take photos? Yes or No")
if Photos=="Yes":
#Add $3 to the bill
    bill +=3
    
    print("f Your final bill is",{bill})

else:
    print("I am sorry! You cannot ride the rollercoaster")





