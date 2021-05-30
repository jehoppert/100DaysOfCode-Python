#working with data
data = []
with open("./weather_data.csv") as file:
  data = file.readlines()
  print(data)

#working with csv data
import csv
with open("./weather_data.csv") as file:
  data = csv.reader(file)
  temperatures = []
  for row in data:
    if row[1] != 'temp':
      temperatures.append(row[1])
  print(temperatures)

#working with csv data with pands
import pandas 
data = pandas.read_csv("./weather_data.csv")
type(data) #data frame
#print(data) #print the data frame
print(data["temp"]) #print the series object

data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)

#average = sum(data_list)/len(data_list)
#print(average)

#pandas math functions
print(data["temp"].mean())
print(data["temp"].max())

#get data in columns
print(data["condition"]) #list reference to the column
print(data.condition) #attribute reference to the column

#get data in rows
print(data[data.day == "Monday"])

#highest temp row
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)

#create data frame from scratch
data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./new_data.csv")

#squirrel Centeral Park color count
#https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#gray_count = 0
#cinnamon_count = 0
#black_count = 0
#for color in squirrel_data["Primary Fur Color"]:
#  if color == "Gray": gray_count += 1
#  if color == "Cinnamon": cinnamon_count += 1
#  if color == "Black": black_count += 1 

gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_count_data_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [gray_count, cinnamon_count, black_count]
}
squirrel_count_data = pandas.DataFrame(squirrel_count_data_dict)
squirrel_count_data.to_csv("./squirrel_count.csv")

