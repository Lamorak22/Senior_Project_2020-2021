# Weather Data Retrieval Program
from wwo_hist import retrieve_hist_data
import urllib.request
import os

# Destination directory
os.chdir("F:\\Daniels Stuff\\Coding Stuff\\Plant recommendation")

# Setting up parameters for the excel file.
# Code taken from https://pypi.org/project/wwo-hist/
frequency=24
start_date = '01-JAN-2010'
end_date = '27-SEP-2020'
api_key = '1354d0c9698c486ea3e191604200408'
location_list = ['97603']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)