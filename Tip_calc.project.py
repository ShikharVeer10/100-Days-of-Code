print("Welcome to the tip calculator project!")
bill=float(input("Enter the total bill? "))
tip=int(input("How much tip would you like to give? 10,12 or $15"))
people=int(input("How many people would like to split the bill? "))
tip_as_percent=tip/100
total_bill_amount=bill+tip_as_percent
bill_per_person=total_bill_amount/people
final=round(bill_per_person,2)
final="{:.2f}".format(bill_per_person)
print(f"Each person should pay: {final} bill in $")
bill_with_tip=tip/10*bill+bill
print(bill_with_tip)