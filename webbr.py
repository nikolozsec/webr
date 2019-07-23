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
    # print(domain)

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

    print(str(domain) + " -  " + str(status) + " - " + str(ip))

# Put output in data
data = {'urls': urlList, 'status': codeList, 'ip': ipList}

# Create a dataframe and write to new excel file
df = pd.DataFrame(data=data, index=None)
print("\n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n" + "= RESULT:                             = \n" + "=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#= \n" + str(df))
writer = ExcelWriter('url_status_ip.xlsx')
df.to_excel(writer,'Sheet1', index=False)
writer.save()