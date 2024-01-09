programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over again",
    "Loop":"Action of doing something over and over again"}

print(programming_dictionary)
print(programming_dictionary["Function"]) #[] brackets are used to take out a specify key from the dictionary
programming_dictionary["Loop"] = "A loop is a programming construct that allows a set of instructions to be repeated multiple times."
print(programming_dictionary)

#To create an empty dictionary
empty_dictionary={}
print(empty_dictionary)

# To edit an item in a dictionary
programming_dictionary["Bug"]="A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
#for thing in programming_dictionary:
 #   print(thing)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict["c"]=[1,2,3]
print(dict["c"])

for key in dict:
    dict[key]+=1
print(dict[key])

