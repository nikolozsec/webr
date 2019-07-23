import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import requests

# File location
src = pd.read_excel('jde_websites.xlsx', sheet_name='Sheet1')

# Count number of rows in excel file
countRow = src.shape[0]

# Print a message
print("webbr Created by Nikoloz Kokhreidze")
print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
print("Checking {} URLs: ".format(countRow))

# Create empty list
urlList = []
codeList = []

# Go throught the File
for i in src.index:
    urlList.append(src['input_urls'][i])
    print(src['input_urls'][i])
    try:
        r = requests.get(src['input_urls'][i])
        status = r.status_code
        codeList.append(status)
        print(status)
    except requests.ConnectionError as error: 
        print(error)
        codeList.append("error")

# Print list of URLs and HTTP Codes
print(urlList)
print(codeList)

# Put output in data
data = {'urls': urlList, 'status': codeList}

# Create a dataframe and write to new excel file
df = pd.DataFrame(data=data, index=None)
print(df)
writer = ExcelWriter('url_checked.xlsx')
df.to_excel(writer,'Sheet1', index=False)
writer.save()