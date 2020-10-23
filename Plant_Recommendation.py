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
        for i in range(x, x + int(plant_time_days[cnt])):
            avg_temp += tmp[i]
    
    #print("avg_temp: ", avg_temp)
    #print("Plant_time_days: ", plant_time_days[cnt])

    return avg_temp/(plant_time_days[cnt]*len(index_list))



# All used variables
index = 0
date = "5/1"
avg_temp = 0
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
to_plant_list = [None] * len(plant)
min_tempC_list = [None] * len(plant)
plant_time_days = [None] * len(plant)


for x in range(0, len(plant)):
    to_plant_list[x] = plant[x]
    plant_time_days[x] = growth_time[x]
    min_tempC_list[x] = min_tempC[x]


# Find all of the indexes of selected date
index_list = [0,0,0,0,0,0,0,0,0,0] 
for x in range(0,len(index_list)):
    index = findDate(index, date)
    # The index variable is the index of each instance of the date
    index_list[x] = index
    index += 1
    

#Print out average temperature for each plant
temp = 0
for x in range(0, len(to_plant_list)):
    avg_temp = 0
    temp = findAvgTempC(index_list, plant_time_days, tmp, avg_temp, x)
    temp = int(temp) #temp is not int. Needs to be an int for if statement
    if temp > int(min_tempC_list[x]):
        print(f"Average temperature is: {temp}, {to_plant_list[x]}'s minimum temperature is {min_tempC_list[x]}, so it is good to plant")
    else:
        print(f"Average temperature is: {temp}, {to_plant_list[x]}'s minimum temperature is {min_tempC_list[x]}, so it is not good to plant")

