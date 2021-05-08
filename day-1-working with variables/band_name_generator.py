print("Welcome to the band name generator") #app greeting
#collect city name and pet name for band name creation
city_name = input("Which city did you grow up in?\n")
pet_name = input("What is a name of a pet you have/had?\n")
#compile city and pet names into the band name
band_name = city_name + " " + pet_name
#let the user know their band name
print("Your band name is: " + band_name)