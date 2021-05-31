#list comprehension
#new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Joe"
new_name = [letter for letter in name]
print(new_name)

rang = range(1,5)
new_rang = [num*2 for num in rang]
print(new_rang)

#conditional list comprehension
#new_list = [new_item for item in list if test]

names = ["Joe", "Lucy"]
new_names = [name.lower() for name in names if len(name) < 4]
print(new_names)

#Coding Challenge 26.1 - list comprehension squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

#Coding Challenge 26.2 - list comprehension filter even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num%2==0]
print(result)

#Coding Challenge 26.3 - list comprehension data overlap
list1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
list2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
result = [num for num in list1 if num in list2]
print(result)

#dictionary comprehension
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items()}
import random
names = ["Joe", "Lucy"]
student_scores = {student:random.randint(0,100) for student in names}
print(student_scores)

passed_students = {student:score for student,score in student_scores.items() if score >= 60}
print(passed_students)

#Coding Challenge 26.4 - dict comprehension letter count
sentence = "What is the airspeed velocity of an unladen swallow?"
word_list = sentence.split(" ")
result = {word:len(word) for word in word_list}
print(result)

#Coding CHallenge 26.5 - dict comprehension temp conversion
weather_c = {
  "Monday": 12,
  "Tuesday": 14,
  "Wednesday": 15,
  "Thursday": 14,
  "Friday": 21,
  "Saturday": 22,
  "Sunday": 24
}
weather_f = {day:temp_c * 9/5 + 32 for day,temp_c in weather_c.items()}
print(weather_f)

#iterate over pandas dataframe
student_dict = {
  "student": ["Joe", "Lucy"],
  "score": [55,66]
}
#looping through dict
for (key,value) in student_dict.items():
  print(value)

import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)

#looping through data frame (rows)
for (index,row) in student_df.iterrows():
  print(row) #pandas series object
  print(row.student) #access the attribute
  print(row.score) #access the attribute
