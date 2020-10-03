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
date = "1/11"
avg_temp = 0
plant_time_months = 3
plant_time_days = 0
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
df2 = pd.read_excel("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\Plant_Database.xlsx")
plant = df2['Plant']
min_tempC = df2['min_tempC']
growth_time = df2['growth_time_days']

print(plant)
print(min_tempC)
print(growth_time)


# Find what you want to plant
print("What would you like to plant?")
input1 = input()
print(input1)

for x in range(0, len(plant)):
    print(x)
    if x == input1:
        plant_time_days = growth_time
        print(plant_time_days)



# Find all of the indexes of selected date
index_list = [0,0,0,0,0]
for x in range(0,len(index_list)):
    index = findDate(index, date)
    index_list[x] = index
    index += 1
    print(index_list)


#Find exact amount of days
# tempvar = date[0]
# tempvar = int(tempvar)
# for i in range(0, plant_time_months):
#     plant_time_days += date_dict[f"{tempvar}"]
#     tempvar += 1
#     print(plant_time_days)

# Get the total temperature from each index for the date
for x in index_list:
    print(type(plant_time_days))
    for i in range(0, plant_time_days):
        #print("Current index: ", x)
        avg_temp += tmp[x]
        #print("Loop #: ", i, "Temp: ", avg_temp)


print(avg_temp/(plant_time_days*len(index_list)))

