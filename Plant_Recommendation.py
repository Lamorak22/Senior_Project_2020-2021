import pandas as pd

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


index = 0
date = "6/1"

plant_time = 3

#Find the date within the dataframe
def findDate(index, date):
    date_flag = False
    
    while date_flag == False:
        result = date_t[index].find(date + '/')
        if result != -1:
            date_flag = True
            print("Date found at index: ", index)
            return index
        else:
            index += 1



# Read the input csv file
df = pd.read_csv("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\97603_24hr.csv")#.set_index('date_time')
date_t = df['date_time']
tmp = df['tempC']


# Find all of the indexes of selected date
index_list = [0,0,0,0,0]
for x in range(0,5):
    index = findDate(index, date)
    index_list[x] = index
    index += 1
    print(index_list)


avg_tmp = 0
for i in range(0, date_dict[f'{date[0]}']):
    avg_tmp += tmp[index]
    index += 1

print("Total temp: ", avg_tmp)
print("Average temperature is", avg_tmp/60, "C")





