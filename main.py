student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# user_input = input("Enter a word:").upper()
# print(user_input)
import csv

# TODO 1. Create a dictionary in this format:
test = {"A": "Alfa", "B": "Bravo"}


# user = input("Enter a word: ")
#
# d = dict()
# f = open("nato_phonetic_alphabet.csv")
# for line in f:
#     line = line.strip('\n')
#     (key, val) = line.split(",")
#     d[key] = val
# print(d)

file = open('nato_phonetic_alphabet.csv')
csv_reader = csv.reader(file)
next(csv_reader)
for row in csv_reader:
    print(row)

#  TODO 2. Create a list of the phonetic code words from a word that the user inputs.

