import pandas as pd

# Dictionary for amount of days for each month
date_dict = {
 '1': 31,
 '2': 28,
 '3': 31,
 '4': 30,
 '5': 31,
 '6': 30,
 '7': 31,
 '8': 31,
 '9': 30,
 '10': 31,
 '11': 30,
 '12': 31}

# All used variables
index = 0
date = "6/1"
avg_temp = 0
plant_time_months = 3
plant_time_days = ["",""]
total_days = 0

#Find the date within the dataframe
def findDate(index, date):
    date_flag = False
    
    while date_flag == False:
        result = date_t[index].find(date + '/')
        if result != -1:
            date_flag = True
            #print("Date found at index: ", index)
            return index
        else:
            index += 1


# Read the file for weather data
df = pd.read_csv("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\97603.csv")#.set_index('date_time')
date_t = df['date_time']
tmp = df['tempC']

# Read the plant database
df2 = pd.read_excel("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\Plant_Database.xlsx", skiprows=0)
plant = df2['Plant']
min_tempC = df2['min_tempC']
growth_time = df2['growth_time_days']

print(plant)


# Parse the database to find the plants in the "to_plant_list"
to_plant_list = ["Tomato", "Onion"]
counter = 0
loopcnt = 0
for x in plant:
    if counter >= len(to_plant_list):
        break
    elif x == to_plant_list[counter]:
        print("Success, found: ", x, "at row: ", loopcnt)
        plant_time_days[counter] = growth_time[loopcnt]
        print("Growth time: ", plant_time_days[counter],"days")
        counter += 1
    loopcnt += 1

print("out of loop")

# Find all of the indexes of selected date
index_list = [0,0,0,0,0]
for x in range(0,len(index_list)):
    index = findDate(index, date)
    index_list[x] = index
    index += 1
    #print(index_list)


#Find exact amount of days
# tempvar = date[0]
# tempvar = int(tempvar)
# for i in range(0, plant_time_months):
#     plant_time_days += date_dict[f"{tempvar}"]
#     tempvar += 1
#     print(plant_time_days)

# Get the total temperature from each index for the date
plant_time_days = int(plant_time_days)
for x in index_list:
    for i in range(0, plant_time_days):
        print("Current index: ", x)
        avg_temp += tmp[x]
        print("Loop #: ", i, "Temp: ", avg_temp)


print(avg_temp/(plant_time_days*len(index_list)))

