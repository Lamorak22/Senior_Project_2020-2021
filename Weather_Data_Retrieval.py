#Weather Data Retrieval Program

from wwo_hist import retrieve_hist_data
#from wwo_hist import hist
import urllib.request
import os


os.chdir("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\temp")

frequency=24
start_date = '01-JAN-2010'
end_date = '01-JAN-2021'
api_key = '0909c9292f294476aba41920211701'
location_list = ['97603']
zipcode = "97603"

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)

if os.path.isfile(f"F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation\\temp\\{zipcode}.csv"):
    print("Exists")
else:
    print("does not exist")