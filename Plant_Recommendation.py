# Plant Recommendation Program for Senior Project 2020-2021
# Daniel Eberhart

import pandas as pd
import datetime

#Find the date within the dataframe
def findDate(index, date):

    while True:
        result = date_t[index].find(date)# .find() will return -1 when false
        if result != -1:
            print("Date found at index: ", index)
            return index 
        else:
            index += 1


def findAvgTempC(index_list, plant_time_days, tempC, avg_temp, cnt):
    # Get the total temperature from each index for the date
    for x in index_list:
        for i in range(x, x + int(plant_time_days[cnt])):
            avg_temp += tempC[i]
    return avg_temp/(plant_time_days[cnt]*len(index_list))


# All used variables
index = 0
avg_temp = 0

# Get tentative planting date
date = "2/2/2021"
d = datetime.datetime.strptime(date, '%m/%d/%Y')
date = d.strftime('%m-%d')
print(date)

# Read the file for weather data and put into dataframe
df = pd.read_csv("97603.csv")#.set_index('date_time')
date_t = df['date_time'] # Variable for list of dates
tempC = df['tempC'] # Variable for average temperature at each date

# Read the plant database
df2 = pd.read_excel("Plant_Database.xlsx", skiprows=0)
plant = df2['Plant'] # Plant names
min_tempC = df2['min_tempC'] # Minimum temperatures for each plant
growth_time = df2['growth_time_days'] # Growth time for each plant


# Create lists
to_plant_list = []
min_tempC_list = []
plant_time_days = []

# Transfer data from pandas over to list format from "class 'pandas.core.series.Series'"
for x in range(0, len(plant)):
    to_plant_list.append(plant[x])
    plant_time_days.append(growth_time[x])
    min_tempC_list.append(min_tempC[x])


# Find all of the indexes of selected date from 2010 to 2020
index_list = [None] * 10
for x in range(0,len(index_list)):
    index = findDate(index, date)
    index_list[x] = index #The index variable is the index of each instance of the date
    index += 1
    

#Print out average temperature for each plant
temp = 0
final_to_plant_list = []
final_dont_plant_list = []
for x in range(0, len(to_plant_list)):
    avg_temp = 0
    temp = findAvgTempC(index_list, plant_time_days, tempC, avg_temp, x)
    temp = int(temp) #temp is not int. Needs to be an int for if statement
    
    if temp > int(min_tempC_list[x]):
        print(f"Average temperature is: {temp}, {to_plant_list[x]}'s minimum temperature is {min_tempC_list[x]}, so it is good to plant")
        final_to_plant_list.append(to_plant_list[x])
    else:
        print(f"Average temperature is: {temp}, {to_plant_list[x]}'s minimum temperature is {min_tempC_list[x]}, so it is not good to plant")
        final_dont_plant_list.append(to_plant_list[x])

print("Good to plant: ", final_to_plant_list)
print("Not good to plant: ", final_dont_plant_list)