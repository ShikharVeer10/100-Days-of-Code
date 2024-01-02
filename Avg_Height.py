student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] =int(student_heights[n])

total_height=0
for height in student_heights:
  total_height+=height
print(f"The total height of the students are :{total_height}")

number_of_students=0
for student in student_heights:
  number_of_students+=1 #Addition of itself
print(f"The total number of students are:{number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
