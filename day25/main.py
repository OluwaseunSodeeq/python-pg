import pandas
# get hold of our data
squirrel_data = pandas.read_csv("./004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# Get the primary fur color of the squirrels
red_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
grey_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"] 
black_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

print(f"Red Squirrels: {len(red_data)}")
print(f"Gray Squirrels: {len(grey_data)}")
print(f"Black Squirrels: {len(black_data)}")

# Create csv file
data = {
    "Fur Color": ["Red", "Gray", "Black"],
    "Count": [len(red_data), len(grey_data), len(black_data)]
}
squirrel_new_data = pandas.DataFrame(data)
squirrel_new_data.to_csv("squirrel_count.csv")
print(squirrel_new_data)