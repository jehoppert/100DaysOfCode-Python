import pandas
#create a dictionary using dict comprehension from the pandas dataframe {"A": "Alpha", "B": "Bravo",...,"Z": "Zulu"}
nato_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

#create a list of the phonetic code words from a word that the user inputs using list comprehension
def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
    phonetic_code_words = [nato_dict[letter] for letter in word]
  except KeyError:
    print("Sorry, only letters in the alphabet please")
    generate_phonetic()
  else:
    print(phonetic_code_words)
    
generate_phonetic()


