import csv

# with open("weather_data.csv") as file:
#     content = file.readlines()
#     print(content)
#
# with open("weather_data.csv") as file:
#     content = csv.reader(file)
#     temperatures = []
#     for row in content:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# # print(data["temp"])
# temp_list = data["temp"].to_list()
# # sum = 0
# for i in temp_list:
#     sum += i
# average = sum(temp_list) / len(temp_list)
# # print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])# treat as a key (map)
# print(data.condition) # treat as attribute
# monday = data[data.day == "Monday"]
# # data[data.temp == data.temp.max()]
# print(monday.condition)
# mondaytemp = monday.temp
# mondaytempF = mondaytemp * 9 / 5 + 32
# print(mondaytempF)

# data_dict = {
#     "students": ["Mukhtar", "Sabina"],
#     "scores": [99, 90],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_txt.csv")

#TODO: create a file called: squirrel_count.csv with tables like Fur Color, Count ,
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])
# data_dict = data.to_list()
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
