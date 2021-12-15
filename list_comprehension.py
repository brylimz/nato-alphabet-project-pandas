import pandas

# # file 1
# file1 = pandas.read_csv("file1.txt")
# new_file1 = file1.values.tolist()
# print(new_file1)
#
# # file 2
# file2 = pandas.read_csv("file2.txt")
# new_file2 = file2.values.tolist()
# print(new_file2)
#
# # List compare
# abc = ""
# result = []
# print(result)
#
#
# # Write your code above 👆

# file 1
with open("file1.txt", mode="r") as file1:
    new_format1 = file1.read().splitlines()
    print(new_format1)

# file 2
with open("file2.txt", mode="r") as file2:
    new_format2 = file2.read().splitlines()

    print(new_format2)

# make a list
result = [int(num) for num in new_format1 if num in new_format2]
print(result)
