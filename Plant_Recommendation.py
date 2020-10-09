import pandas as pd

#Find the date within the dataframe
def findDate(index, date):
    date_flag = False
    while date_flag == False:
        # .find() will return -1 when false
        result = date_t[index].find(date + '/')
        if result != -1:
            date_flag = True
            print("Date found at index: ", index)
            return index 
        else:
            index += 1

def findAvgTempC(index_list, plant_time_days, tmp, avg_temp, cnt):
    # Get the total temperature from each index for the date
    for x in index_list:
        for i in range(0, int(plant_time_days[cnt])):
            avg_temp += tmp[x]
    
    return avg_temp/(plant_time_days[cnt]*len(index_list))



# All used variables
index = 0
date = "6/1"
avg_temp = 0
plant_time_months = 3
total_days = 0

# Read the file for weather data
df = pd.read_csv("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\97603.csv")#.set_index('date_time')
date_t = df['date_time'] # List of dates
tmp = df['tempC'] # Average temperature for each date

# Read the plant database
df2 = pd.read_excel("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\Plant_Database.xlsx", skiprows=0)
plant = df2['Plant'] # Plant names
min_tempC = df2['min_tempC'] # Minimum temperatures for each plant
growth_time = df2['growth_time_days'] # Growth time for each plant

# Parse the database to find the plants in the "to_plant_list"
to_plant_list = ["Tomato", "Onion"]
plant_time_days = [None] * len(to_plant_list)
min_tempC_list = [None] * len(to_plant_list)

counter = 0
loopcnt = 0
for x in plant:
    if counter >= len(to_plant_list):
        break
    elif x == to_plant_list[counter]:
        print("Success, found: ", x, "at row: ", loopcnt)
        plant_time_days[counter] = growth_time[loopcnt]
        min_tempC_list[counter] = min_tempC[loopcnt]
        print("Growth time: ", plant_time_days[counter], "days")
        print("Growth temperature: ", min_tempC_list[counter], "degrees C")
        counter += 1
    loopcnt += 1

print("out of loop")

# Find all of the indexes of selected date
index_list = [0,0,0,0,0] # Only using 5 date indexes right now
for x in range(0,len(index_list)):
    index = findDate(index, date)
    # The index variable is the index of each instance of the date
    index_list[x] = index
    index += 1
    

#Print out average temperature for each plant
temp = 0
for x in range(0, len(to_plant_list)):
    temp = findAvgTempC(index_list, plant_time_days, tmp, avg_temp, x)
    temp = int(temp) #temp is not int. Needs to be an int for if statement
    if temp > int(min_tempC_list[x]):
        print("Good to plant")
    else:
        print("Not good to plant")

