student_marks=input().split()
for n in range(0, len(student_marks)):
  student_marks[n] =int(student_marks[n])

total_mark=0
for marks in student_marks:
  total_mark+=marks
print(f"The total marks are {total_mark}")

number_of_students=0
for number_of_students in student_marks:
  number_of_students +=1
print(f"The total number of students = {number_of_students} ")

average_marks=round(total_mark/number_of_students)
print(f"The average marks gained by the class are {average_marks} ")