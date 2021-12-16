
# Iterate over a pandas Data Frame
student_dict = {
    "student": ["angela", "james", "lily"],
    "score": [56, 76, 98]
}
# for (key, value) in student_dict.items():
#     print(key, value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


# loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# loop throught rows of a date frame
for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela".lower():
        print(row.score)