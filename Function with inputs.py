#Task: 
#Create a function called greet
#Write 3 print statements inside the function
# Call the greet() function and run your code
def greet():
    print("Hello")
    print("Bye")
    print("Hello Bye")
print(greet())

def greet():
    print("Hello Shikhar")
    print("How do you do Shikhar?")
    print("Where are you going?")
print(greet())

#Function that allows for an input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Where are you from? {name}")
    print(f"What are you hobbies {name}?")
print(greet_with_name("Shikhar"))

# Functions with more than 1 input
def greet_with_noname(name,age,location):
    print(f"Hello {name}")
    print(f"Where are you from? {location}")
    print(f"I am {age} years old")
print(greet_with_noname("Shikhar V","19", "I am from Hyderabad"))

#Keyword Arguments
def greet_with_noname(name="Shikhar",age="19",location="Hyderabd"):
    print(f"Hello {name}")
    print(f"Where are you from? {location}")
    print(f"I am {age} years old")
print(greet_with_noname("Shikhar V","19", "I am from Hyderabad"))

#Positional Arguements
def greet_with_noname(name,age,location):
    print(f"Hello {name}")
    print(f"What is you age?{age}")
    print(f"Where are you from?{location}")
print(greet_with_noname("Shikhar V","19","London")) # Positional Arguements

def greet_with_Name(Name,Age,Sport):
    print(f"Hello {Name}")
    print(f"What is your age?{Age}")
    print(f"What is you favourite sport?{Sport}") 
print(greet_with_Name("Shikhar V","19","Cricket"))

def interview_question(Name,Occupation,Work):
    print(f"What is your Name?{Name}")
    print(f"What occupation do you look to work in?{Occupation}")
    print(f"Do you have any Work experience under this occupation in the recent years?{Work}")
print(interview_question("Shikhar V","AI/ML Engineer","Yes"))
