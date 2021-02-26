#!/usr/bin/python3
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import json
import sys
import pandas as pd
import logging
from wwo_hist import retrieve_hist_data
import os
import datetime

sys.path.append("/home/pi/.local/lib/python3.7")

import plantrec


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

@app.route("/prp", methods=['GET','POST','OPTIONS'])
@cross_origin()
def prp():
    date = request.args.get('date_string')
    zipcode = request.args.get('zipcode_str')
     
    os.chdir("/var/www/FlaskApp/FlaskApp")

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

    if os.path.isfile(f"/var/www/FlaskApp/FlaskApp/{zipcode}.csv"):
        data3 = "PRP API call Success"
        prplist = plantrec.prpmain(date)
    else:
        data3 = "PRP API call Failure"


    temp = {
            "date" : date,
            "zip" : zipcode,
            "prp" : prplist
            }
    y = json.dumps(temp)
    return y

@app.route("/sensor", methods=['GET', 'OPTIONS'])
@cross_origin()
def sensor():
    GPIO.setmode(GPIO.BCM)
    sms = 17
    ldr = 23

    #LDR
    def ldrfunc(ldr):
        count = 0
        GPIO.setup(ldr,GPIO.OUT)
        GPIO.output(ldr,GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(ldr,GPIO.IN)

        while (GPIO.input(ldr) == GPIO.LOW):
            count += 1
        return count
    ldrval = ldrfunc(ldr)
    
    #SMS
    resultsms = 0
    GPIO.setup(sms, GPIO.IN)
    if GPIO.input(sms):
        resultsms = "No Moisture Detected"
    else:
        resultsms = "Moisture Detected"

    #DHT11
    tempsensor=Adafruit_DHT.DHT11
    tempsensorgpio = 4
    humidity, tempC = Adafruit_DHT.read_retry(tempsensor,tempsensorgpio)
    tempF = tempC * 9/5 + 32
    
    #Create current time variable
    #curr_time = time.localtime(time.time())
    #date = str(curr_time[3]) + ":" + str(curr_time[4]) + ", " + str(curr_time[1]) + "/" + str(curr_time[2]) + "/" + str(curr_time[0]) 

    sensor_dict = {
            "resultsms": resultsms,
            "ldr": ldrval,
            "humidity": humidity,
            "tempC": tempC,
            "tempF": tempF
            }
    y = json.dumps(sensor_dict)
    
    return y 

if __name__ == "__main__":
    app.run()
