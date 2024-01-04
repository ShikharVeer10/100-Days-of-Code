
import math
def paint_calc(test_h,test_w,coverage):
  print(f"What is the height of the wall?{test_h}")
  print(f"What is the width of the wall?{test_w}")
  print(f"What is the coverage of the wall?{coverage}")
  def paint_calc (number_of_cans,round_up_cans):
    number_of_cans=input()
    round_up_cans=input()
  number_of_cans=(test_h*test_w)/coverage
  round_up_cans=math.ceil(number_of_cans) ##
  print(f"You will need {round_up_cans} cans of paint ")
print(paint_calc(9,4,5))


#Code below to not be changed
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage=5
paint_calc(height=test_h, width=test_w, cover=coverage)

