## Lets Play with Pandas

import csv
import pandas as pd

# Ancient way to deal with files ...
print("\nOPEN METHOD")
with open("./day_25/weather_data.csv") as file:
    content = file.read()
    print(content)
    file.close()

# Another way, using csv library
import csv
print("\nCSV LIB")
with open("./day_25/weather_data.csv") as file:
    content = csv.reader(file)
    print(content) # print object, not content
    for row in content: # now you print the actual content, row by row
        print(row)

# Newer and more efficient way, using Pandas library
import pandas as pd  
print("\nPANDAS LIB")
weather = pd.read_csv("./day_25/weather_data.csv")
print(weather)

# or, using its methods
print("\n head")
print(weather.head(3))
print("\n tail")
print(weather.tail(3))

print("\n dtype")
print(weather.dtypes)

print("\n info")
print(weather.info)

print("\n selecting a column")
print(weather["day"])
# or print(weather.day)

print("\n dataframe to other data type inbuild function")
dict_weather = weather.to_dict()
print(dict_weather)

print("\n finding statistic data")
average_temp = sum(weather["temp"])/len(weather["temp"])
average_temp_pd = weather["temp"].mean()
print(f"{average_temp} must be equal to {average_temp_pd}\n")


## Selecting Collumns and Rows
#Getting temperature collumn data
temp_col = weather["temp"]
print(temp_col)
#Getting rows with temperature > 20 degrees
temp_hot_row = weather[weather["temp"] >= 20]
print(temp_hot_row)
