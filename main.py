"""student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
"""
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letters_dict = data.to_dict()
phonetic_dict = {row.letter: row.code for (index, row)in data.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

#word_list = [letter for letter in word]
#print(word_list)
input_word = True
while input_word:
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        word = input("Enter a word: ").upper()
    else:
        print(phonetic_list)
        input_word = False