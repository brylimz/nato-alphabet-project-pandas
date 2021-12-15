# # numbers = [1, 2, 3]
# # new_numbers = [n + 1 for n in numbers]
# # print(new_numbers)
#
# # new_bobo = []
# # for n in numbers:
# #     hehe = n + 1
# #     new_bobo.append(hehe)
# #     print(new_bobo)
#
# name = "Angela"
# new_list = [letter for letter in name]
#
# # new_numbers = [i for i in range(1, 10) if i % 2 == 0]
# # print(new_numbers)
# range_list = [new_item * 2 for new_item in range(1, 5)]
# print(range_list)
#
# name = ["Jhonny", "Bruno", "Ripper", "Ben"]
# new_candidate = [i.upper() for i in name if len(i) < 5]
# print(new_candidate)
number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_number = [i*i for i in number]

print(squared_number)
