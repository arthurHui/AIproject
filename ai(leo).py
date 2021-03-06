# -*- coding: utf-8 -*-
"""AI(leo).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T_-Dffc8glI4I8G96_7pcSOUc4R2Fej9
"""

# -*- coding: utf-8 -*-

import pandas as pd
from numpy import *
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import io
import pylab, random

#use selenium to do web crawler from hko web side
!pip install selenium
!apt-get update 
!apt install chromium-chromedriver

from selenium import webdriver
from bs4 import BeautifulSoup
import time
 
#PATH = "C:\Program Files (x86)\chromedriver.exe"
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)

lightningDays = {}
lightningDays['recordedLightning'] = []
lightningDays['recordedLightning1'] = []
lightningDays['recordedLightning2'] = []
lightningDays['recordedLightning3'] = []
lightningDays['recordedLightning4'] = []
lightningDays['recordedLightning5'] = []
lightningDays['recordedLightning6'] = []
lightningDays['recordedLightning7'] = []
lightningDays['recordedLightning8'] = []
lightningDays['recordedLightning9'] = []
lightningDays['recordedLightning10'] = []
lightningDays['recordedLightning11'] = []
lightningDays['recordedLightning12'] = []
lightningDays['recordedRainfall'] = []
lightningDays['recordedRainfall1'] = []
lightningDays['recordedRainfall2'] = []
lightningDays['recordedRainfall3'] = []
lightningDays['recordedRainfall4'] = []
lightningDays['recordedRainfall5'] = []
lightningDays['recordedRainfall6'] = []
lightningDays['recordedRainfall7'] = []
lightningDays['recordedRainfall8'] = []
lightningDays['recordedRainfall9'] = []
lightningDays['recordedRainfall10'] = []
lightningDays['recordedRainfall22'] = []
lightningDays['recordedRainfall23'] = []

driver.get("https://www.hko.gov.hk/tc/cis/statistic/lgday_statistic.htm")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
titlesLightning = soup.find_all('td')

for i in range(0, len(titlesLightning)-78, 14):
  lightningDays['recordedLightning'].append(titlesLightning[i+1].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+2].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+3].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+4].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+5].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+6].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+7].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+8].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+9].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+10].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+11].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+12].getText())
  lightningDays['recordedLightning'].append(titlesLightning[i+13].getText())
  
driver.get("https://www.hko.gov.hk/tc/cis/statistic/rf_25.htm")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
titlesRainfall = soup.find_all('td')

for a in range(770, len(titlesRainfall)-90, 14):
  lightningDays['recordedRainfall'].append(titlesRainfall[a+1].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+2].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+3].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+4].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+5].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+6].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+7].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+8].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+9].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+10].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+11].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+12].getText())
  lightningDays['recordedRainfall'].append(titlesRainfall[a+13].getText())


driver.quit()

def getLightningData():
    lightningData = {}
    lightningData['lightning'] = []
    for i in range(len(lightningDays['recordedLightning'])):
      if str(lightningDays['recordedLightning'][i]) != '\xa0':
        lightningData['lightning'].append(int(lightningDays['recordedLightning'][i]))
        if str(lightningDays['recordedLightning'][i]) == "-":
          lightningData['lightning'].append(0)
        else:
          lightningData['lightning'].append(int(lightningDays['recordedLightning'][i]))
      
    return lightningData['lightning']

def getRainfallData():
    rainfallData = {}
    rainfallData['Rainfall'] = []
    for i in range(len(lightningDays['recordedRainfall'])):
      if str(lightningDays['recordedRainfall'][i]) != '\xa0':
        rainfallData['Rainfall'].append(int(lightningDays['recordedRainfall'][i]))
        if str(lightningDays['recordedRainfall'][i]) == "-":
          rainfallData['Rainfall'].append(0)
        else:
          rainfallData['Rainfall'].append(int(lightningDays['recordedRainfall'][i]))

    return rainfallData['Rainfall']

plt.scatter(getRainfallData(),getLightningData())
plt.xlabel('Days of Rainfall')
plt.ylabel('Days of Lightning')
plt.title('Relationship between lightning & rainfall(1947-2020)')
plt.show

