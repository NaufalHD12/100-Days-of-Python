# with open("Day25/weather_data.csv") as file:
#     list_data = file.readlines()
#     print(list_data)

# import csv

# with open("Day25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(row[1])
    
#     print(temperatures)
        

import pandas as pd
data = pd.read_csv("Day25/weather_data.csv")
# print(data)
# print()
# print(data['condition'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)

# # or
# print(data["temp"].mean())

# # maximum value
# print(f"Max: {data['temp'].max()}")

# # Get data in columns
# print(data['condition'])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(int(monday.temp) * 1.8 + 32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

## Squirrel Sensus
data = pd.read_csv("Day25/squirrel_data.csv")
grey_count = (data['Primary Fur Color'] == "Gray").sum()
red_count = (data['Primary Fur Color'] == "Cinnamon").sum()
black_count = (data['Primary Fur Color'] == "Black").sum()


data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Counts": [grey_count, red_count, black_count]
}
new_df = pd.DataFrame(data_dict)
print(new_df)
new_df.to_csv("squirrel_count.csv")