import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import requests

src = pd.read_excel('url.xlsx', sheet_name='Sheet1')

values = src['websites'].values

countRow = src.shape[0]

print("Checking {} URLs: ".format(countRow))

urlList = []
codeList = []

for i in src.index:
    urlList.append(src['websites'][i])
    try:
        r = requests.get(src['websites'][i])
        status = r.status_code
        codeList.append(status)
    except requests.exceptions.RequestException as error: 
        print(error)
        codeList.append("error")


print(urlList)
print(codeList)

urlArray = np.asarray(urlList)
codeArray = np.asarray(codeList)
print(urlArray)

df = pd.DataFrame({'urls': [urlArray],'codes':[codeArray]})
writer = ExcelWriter('url_checked.xlsx')
df.to_excel(writer,'Sheet1', index=False)
writer.save()

# try:
#     r = requests.get('http://www.google.com/nothere')
#     r.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print err
#     sys.exit(1)


    # print(src['websites'][i])
    # r = requests.get(src['websites'][i])
    # print(r.status_code)
    # df = pd.DataFrame({'urls':src['websites'][i],
    #                'codes':[r]})
    # writer = ExcelWriter('url_checked.xlsx')
    # df.to_excel(writer,'Sheet1',index=False)
    # writer.save()
    
# i = 0
# while i < count_row :
#     list.append
#     print(src['websites'][i])
#     i += 1

#listWebsites = df['websites']
#print(listWebsites[0])