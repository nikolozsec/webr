import os
import sys
import socket
from datetime import datetime
import requests
import tldextract
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define time for unique screenshot names
screenshotTime = datetime.strftime(datetime.now(), ' %Y-%m-%d %H-%M-%S')

# Chrome Driver configuration for taking screenshots
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")  
chrome_options.add_argument("--disable-extensions") 
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_driver = '.\\driver\\chromedriver.exe'

# Ask for screenmshots
takeScreens = input("Take website screenshots? (Chrome required) [1] For all websites [2] Only for errors [3] None:  ")

# Ask for file
inputFile = input("Source excel file:  ")
outputFile = input("Destination excel file: ")

# File location
src = pd.read_excel(inputFile)

# Count number of rows in excel file
countRow = src.shape[0]

# Create empty list
urlList = []
codeList = []
ipList = []

# Print a message
print("\n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n" + "=     webbr by Nikoloz Kokhreidze     = \n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n")
print("CHECKING {} ITEMS: \n".format(countRow))

# Go throught the File
for i in src.index:

# Extract domain from URL
    domain_extract = tldextract.extract(src['input_urls'][i])
    domain = domain_extract.domain + '.' + domain_extract.suffix

# Check URLs and add them to the list
    urlList.append(domain)

# Get IP from domain
    try:
        ip = socket.gethostbyname(domain)
        ipList.append(ip)

# If error, write error in excel
    except socket.error as error:
        ipList.append("error")
        ip = "error"

# Try to send request
    try:
        r = requests.get(src['input_urls'][i], stream=True)
        status = r.status_code
        codeList.append(status)

# If error, write error in excel
    except requests.ConnectionError as error: 
        codeList.append("error")
        status = "error"

# Take screenshots based on user input
    if takeScreens == '1':
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        driver.get(src['input_urls'][i])
        driver.save_screenshot('.\\screenshots\\' + domain + screenshotTime + '.png')
        driver.close()

    elif takeScreens == '2' and status != 200:
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        driver.get(src['input_urls'][i])
        driver.save_screenshot('.\\screenshots\\' + domain + screenshotTime + '.png')
        driver.close()

    print(str(domain) + " -  " + str(status) + " - " + str(ip))

# Put output in data
data = {'urls': urlList, 'status': codeList, 'ip': ipList}

# Create a dataframe and write to new excel file
df = pd.DataFrame(data=data, index=None)
print("\n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n" + "= RESULT:                             = \n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n" + str(df))
writer = ExcelWriter(outputFile)
df.to_excel(writer,'Sheet1', index=False)
writer.save()