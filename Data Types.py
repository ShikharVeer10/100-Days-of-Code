# Primitive Data Types
#String
#Float:When a decimal point is included in a number, it is said to be as a float function
#Subscript: Pulling a particular element from a string
print(len("Ashok"))
print("Hello"[0])
print("Hello"[4])
print("Shikhar"[3])
print("Messi"[4])
print("Hello"[4])
print("123" + "345") #Concat Function: Concentrating 2 strings when string function is used
two_digit_number=input()
first_digit=int(two_digit_number[0])
second_digit=int(two_digit_number[1])
two_digit_number=first_digit + second_digit   # Add the two integers together
print(two_digit_number)

#b=int(input("Enter any two digit number:"))
#first_digit_number=int(input(two_digit_number[0]))
#second_digit_number=int(input(two_digit_number[1]))
#two_digit_number=first_digit_number+second_digit_number
#print(type((two_digit_number)))
num_char=len(input("What is your name?")) # Integer data type is put inside a string data type
#Len gives an integer data type
new_num_char=str(num_char)
print("Your name has "  + new_num_char +  " characters")
print(70 + float("100.5"))
print(str(70) + str(100)) # Concatenates both the string as it is a alphabetical data type "+"