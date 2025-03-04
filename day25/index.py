# with open("./002 weather-data.csv") as data:
#     data = data.readlines()
#     print(data)

import csv
with open("./002 weather-data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        # print(row)
        if row[1] !=  'temp':
            new_row = int(row[1])
            temperatures.append(new_row)
            # print(temperatures)

import pandas
data = pandas.read_csv("./002 weather-data.csv")
# print(data["temp"])
# print(f" Mean : {data["temp"].mean()}")
# To convert the data to dictionary
data_dict = data.to_dict()
print(f"Data converted to Dictionary :{data_dict}")

# to convert the temp to list
data_list = data["temp"].to_list()
data_list_of_condition = data["condition"].to_list()
print(f"Data converted to List :{data_list}")
print(f"Data converted to List of Condition :{data_list_of_condition}")

# Challenge: Calculate the Average/Mean of the temp list
cur_temp = 0
for temp in data_list:
    cur_temp += temp
average_temps = cur_temp / len(data_list)
print(f"Average temperature is : {average_temps}")

# average_temps = sum(data_list) / len(data_list)
# average_temps = data_list.mean()
max_temp = data["temp"].max()

# Pull out data of weather condition
print(data[data.condition == "Rain"])
print(data[data.condition == "Sunny"])
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp = monday.temp
# converting_to_fahrenheit
monday_temp_to_fahrenheit = monday_temp * 9/5 + 32
print(f"Deg: {monday.temp }\n Fahrenheit : {monday_temp_to_fahrenheit}")

# Create a dataframe from scratch
user_data ={
    "students": ["Oluwaseun", "Oluwatobiloba", "Oluwatoyin"],
    "scores": [90, 80, 70]
}

new_data = pandas.DataFrame(user_data)

# To covert to CSV and create new file for it
new_data.to_csv("new_data.csv")
print(new_data)