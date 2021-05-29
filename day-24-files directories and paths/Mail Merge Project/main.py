#create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter_file:
    starting_letter_text = starting_letter_file.read()

#collect all the invited names
with open("./Input/Names/invited_names.txt", mode="r") as invited_names_file:
    invited_names_list = invited_names_file.readlines()
    
#for each name in invited_names.txt
for name in invited_names_list:
    #Replace the [name] placeholder with the actual name.
    person = name.strip("\n")
    output_letter_text = starting_letter_text.replace("[name]", person)

    #Save the letters in the folder "ReadyToSend"
    with open(f"./Output/ReadyToSend/{person}_letter.txt", mode="w") as output_letter_file:
        output_letter_file.write(output_letter_text)