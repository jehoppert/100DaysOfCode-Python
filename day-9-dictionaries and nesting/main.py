#9.1 Coding Challenge - grading program
student_score = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62
}
print(student_score)

student_grades = {}

for student in student_score:
  if student_score[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_score[student] > 80:
    student_grades[student] = "Exceeds Expectations"
  elif student_score[student] > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

#9.2 Coding Challenge - dictionary in list
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  }
]

def add_new_country(country, visits, cities):
  travel_log.append(
    {
      "country": country,
      "visits": visits,
      "cities": cities
    }
  )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)