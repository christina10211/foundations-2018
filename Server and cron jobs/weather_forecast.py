
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get('https://api.darksky.net/forecast/APIKEY/40.7447,-73.9485?units=si')
data =response.json()


# In[3]:


data


# In[4]:


#Right now it is TEMPERATURE degrees out and SUMMARY. 
#Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.


current_temp = data['currently']['temperature']
summary = data['currently']['summary'].lower()

forecast_daily=data['daily']['data'][0]
temp_high = forecast_daily['temperatureHigh']
temp_feeling =''
if temp_high <20:
    temp_feeling = 'cold'
elif temp_high <25:
    temp_feeling = 'warm'
elif temp_high <40:
    temp_feeling = 'hot'

temp_low =forecast_daily['temperatureLow']

rain_warning = ''
if forecast_daily['icon'] == 'rain':
    rain_warning = "It's going to rain today. Bring your umbrella."


# In[5]:


msg = 'Right now it is ' + str(current_temp) + ' degrees out and '+ summary +'.' +' Today will be ' + temp_feeling + ' with a high of ' + str(temp_high) + ' degrees and a low of ' + str(temp_low) + ' degrees. ' + rain_warning


# In[6]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %d, %Y.")


# In[7]:


date_string


# In[8]:


"8AM Weather Forecast: "+date_string


# In[9]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox069bc2aaa4974001b7b17a41ecef39d0.mailgun.org/messages",
        auth=("api", "43bb3bf155c898d293ccccc7dd16fce3-0470a1f7-1fcbc759"),
        data={"from": "Little Little <mailgun@sandbox069bc2aaa4974001b7b17a41ecef39d0.mailgun.org>",
              "to": ["zz2564@columbia.edu"],
              "subject": "8AM Weather Forecast: "+date_string,
              "text": msg}) 
response.text

