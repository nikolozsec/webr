import requests
import socket
import tldextract
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# File location
src = pd.read_excel('websites.xlsx', sheet_name='Sheet1')

# Count number of rows in excel file
countRow = src.shape[0]

# Print a message
print("webbr Created by Nikoloz Kokhreidze")
print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("Checking {} URLs: ".format(countRow))

# Create empty list
urlList = []
codeList = []
ipList = []

# Go throught the File
for i in src.index:

# Check URLs and add them to the list
    urlList.append(src['input_urls'][i])
    print(src['input_urls'][i])

# Extract domain from URL
    domain_extract = tldextract.extract(src['input_urls'][i])
    domain = domain_extract.domain + '.' + domain_extract.suffix
    print(domain)

# Get IP from domain
    try:
        ip = socket.gethostbyname(domain)
        ipList.append(ip)
        print(ip)

# If error, write error in excel
    except socket.error as error:
        print(error)
        ipList.append("error")

# Try to send request
    try:
        r = requests.get(src['input_urls'][i], stream=True)
        status = r.status_code
        codeList.append(status)
        print(status)

# If error, write error in excel
    except requests.ConnectionError as error: 
        print(error)
        codeList.append("error")

# Put output in data
data = {'urls': urlList, 'status': codeList, 'ip': ipList}

# Create a dataframe and write to new excel file
df = pd.DataFrame(data=data, index=None)
print(df)
writer = ExcelWriter('url_status_ip.xlsx')
df.to_excel(writer,'Sheet1', index=False)
writer.save()