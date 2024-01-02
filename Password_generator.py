print("Welcome to the password generator!")
import random
letters=['a','b''c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*']
nr_letters=int(input(f"How many letters would you like in your password?\n"))
nr_numbers=int(input(f"How many numbers would you like in your password?\n"))
nr_symbols=int(input(f"How many symbols would you like in your password?\n"))

Password=""

#Hard level
Password_list=[]
for char in range(1,nr_letters+1): #Char function: Returns the characters in a string
    Password_list.append(random.choice(letters)) #Append Function: Adds the element the end in the existing list
    
for char in range(1,nr_symbols+1):
    Password_list +=random.choice(symbols)

for char in range(1,nr_numbers+1):
    Password_list +=random.choice(numbers)

print(Password_list)
random.shuffle(Password_list) #Shuffles the password every time
print(Password_list)

