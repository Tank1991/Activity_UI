import requests
import urllib3
urllib3.disable_warnings()

url = 'https://test34.maxuscloud.cn/ampService/api/activityApiController/querySynActivityInfo'

body ={
    "updateDateBegin" : "2018-12-01",
    "updateDateEnd" : "2018-12-31",
    "reqSysMark" : "clm"
}

r = requests.post(url ,json=body , verify =False)

print(r.status_code)