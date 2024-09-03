with open("/Users/shikh/OneDrive/Desktop/my_file.txt") as file:
    contents=file.read() #Access through the file
    print(contents) # Print or read the contents through the file
    
with open("new_file.txt",mode="a") as file: #a as Append means add the text in the file
    file.write("\n New text")

    