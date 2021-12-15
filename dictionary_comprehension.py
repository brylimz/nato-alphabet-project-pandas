# import random
# names = ['alex', 'beth', 'caroline', 'dave', 'elenora', 'freddie']
# # student_scores ={new_key:new_value for item in names}
# student_scores ={student_score: random.randint(1, 100) for student_score in names}
# print(student_scores)
# # passed_students = {new_key:new_value for (key,value) in dictionary.items if score()}
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# exercise
sentence = "What is the Airspeed Velocity of an Unladen Shallow?"
split_sentence = sentence.split()
result = {sentence: len(sentence) for sentence in split_sentence}
print(result)