#Random integer
import random
random_integer=random.randint(1,100) #When printing a random integer we use the function randint
print(random_integer) # This program is used to print any random integer between the start values and the end values


#Random Float Number
import random
random_float=random.randrange(1,100) #Rand any 2 numbers
print(random_float)

#Random Float Number(Integer(Decimal Format))
import random
random_float=random.random() #Known to be as a uniform function
print(random_float)

#Random Decimal Number between 1.1 and 1.5
import random
random_float=random.uniform(1.1,1.5) #Unifrom function: A function to get a decimal number between 2 float numbers
print(random_float)

#Random decimal number between 0 and 5
import random
random_float=random.uniform(0.0,5.0)
print(random_float)

#Random decimal number between 0.0 and 1.0
import random
random_float=random.uniform(0.0,1.0)
print(random_float)
print(random_float*5)

love_Score=random.randint(1,100)
print(f"Your love score is {love_Score}")