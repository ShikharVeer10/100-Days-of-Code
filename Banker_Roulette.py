names_string=input()
names=names_string.split(",")
import random
num_of_people=len(names) #Total no of names in the list
print(names)
random_choice=random.randint(0,num_of_people-1)#Code to generate a random choice
person_who_will_pay_the_bill=names[random_choice]
print(person_who_will_pay_the_bill+ " is going to buy the meal today")