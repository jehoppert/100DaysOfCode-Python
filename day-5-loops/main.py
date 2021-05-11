#5.1 Coding Challenge - average height
student_heights = input("Input a list of student heights\n").split()
#for hieght in student_heights:
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
count = 0
for h in student_heights:
  count += 1
  total += h

average = round(total/count)
print(average)

#5.2 Coding Challenge - High Score
student_scores = input("Input a list of student score\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

high_score = 0
for score in student_scores:
  if high_score < score:
    high_score = score

print(f"The highest score in the class is: {high_score}")

#5.3 Coding Challenge - Adding Even Numbers
total = 0
for i in range(2,101,2):
  total += i
print(total)

#5.4 Coding Challenge - FizzBuzz job interview
for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)