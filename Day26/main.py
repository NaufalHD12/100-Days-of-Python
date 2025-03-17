# # List comprehensions
# numbers = [1, 2, 3]
# new_numbers = [num + 1 for num in numbers]
# print(new_numbers)

# name = "Naufal"
# letter_lists = [letter for letter in name]
# print(letter_lists)

# doubled_list = [num * 2 for num in range(1, 5)]
# print(doubled_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# # squaring numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# # Filtering Even Numbers
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# # Data Overlap
# # 💪 This exercise is HARD 💪 

# # Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

# # You are going to create a list called result which contains the numbers that are common in both files. 

# # e.g. if file1.txt contained: 

# # 1 

# # 2 

# # 3

# # and file2.txt contained: 

# # 2

# # 3

# # 4

# # result = [2, 3]
# with open("file1.txt") as file1:
#     list_num1 = file1.read().splitlines()

# with open("file2.txt") as file2:
#     list_num2 = file2.read().splitlines()
    
    
# result = [int(num) for num in list_num1 if num in list_num2]

# print(result)

# # Dictionary Comprehension
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
# passed_students = {student: score for student, score in student_scores.items() if score >= 60}
# print(passed_students)

# # Dictionary Comprehension 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# # Dictionary Comprehension 2
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {day: round(temp * 1.8 + 32, 1) for day, temp in weather_c.items()}

# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key)

import pandas as pd

student_df = pd.DataFrame(student_dict)
print(student_df)
print()
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
    