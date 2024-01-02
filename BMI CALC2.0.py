height=float(input("Enter the height: "))
weight=int(input("Enter the weight: "))
bmi=weight/(height*height)
if bmi<18:
    print(f"Your BMI is {bmi},you are underweight.")
elif bmi<25:
    print(f"Your BMI is {bmi},you have a normal weight")
elif bmi<30:
    print(f"Your BMI is {bmi},you are slightly overweight")
elif bmi<35:
    print(f"Your BMI is {bmi},you are obese")
else:
    print(f"Your BMI is {bmi},you are clinically Obese")