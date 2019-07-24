import os
import socket
import platform
import requests
import tldextract
import pandas as pd
from datetime import datetime
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
chrome_options.add_argument("--window-size=1366,768")
chrome_options.add_argument("--disable-dev-shm-usage")

# Check OS and use relevant driver
if platform.system() == 'Windows':
    chrome_driver = '.\\driver\\chromedriver.exe'
else:
    chrome_driver = './driver/chromedriver'

# Ask for screenshots
takeScreens = input("Take website screenshots? (Chrome required) [1] For all websites [2] Only for non HTTP 200 responses (for errors) [3] No screenshots: ")

# Ask for file
inputFile = input("Source excel file:  ")
inputColumn = input("Column header:  ")
outputFile = input("Destination excel file: ")

# File location
src = pd.read_excel(inputFile)
column = src[inputColumn]

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

# Separates the gTLD or ccTLD from the registered domain and subdomains of a URL
    domain_extract = tldextract.extract(column[i])
    domain = domain_extract.domain + '.' + domain_extract.suffix
    httpUrl = 'http://' + domain

# Add URLs to the list
    urlList.append(httpUrl)

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
        r = requests.get(httpUrl, stream=True)
        status = r.status_code
        codeList.append(status)

# If error, write error in excel
    except requests.ConnectionError as error: 
        codeList.append("error")
        status = "error"

# Take screenshots based on user input
    if takeScreens == '1':
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        driver.get(column[i])
        driver.save_screenshot('.\\screenshots\\' + domain + screenshotTime + '.png')
        driver.close()

    elif takeScreens == '2' and status != 200:
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        driver.get(column[i])
        driver.save_screenshot('.\\screenshots\\' + domain + screenshotTime + '.png')
        driver.close()

    print(str(domain) + " -  " + str(status) + " - " + str(ip))

# Put output in data
data = {'URL': urlList, 'Status': codeList, 'IP': ipList}

# Create a dataframe and write to new excel file
df = pd.DataFrame(data=data, index=None)
print("\n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n" + "= RESULT:                             = \n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n" + str(df))
writer = ExcelWriter(outputFile)
df.to_excel(writer,'webbr', index=False)
writer.save()