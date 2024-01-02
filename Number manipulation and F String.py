print(8/3) #Printing the output in the form of decimal
print(round(8/3)) #Rounding off the output
print(int(8/3))
print(type(8/3)) #Printing the form of the output
print(type(8//3))   
result=4/2
result/=2
print(result)

# F- Strings # A function in which the value is defined inside the bracket for string literals for formatting
score=0
height=1.8
isWinning=True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#F-strings(4000 weeks)
age=int(input("Enter age:"))
years=90-int(age)
weeks=years*52
print(f"you have {weeks} weeks left")