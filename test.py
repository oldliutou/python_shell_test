import json

import requests
# 101080101 呼市
# 101120101  济南
url = "http://t.weather.sojson.com/api/weather/city/101120101" # 济南
r = requests.get(url).text
print(r)

data2 = json.loads(r)
print(data2["data"]['forecast'][0])
print(data2["data"]['forecast'][0]["high"])
print(data2["data"]['forecast'][0]["low"])
print("今天是什么日子："+data2["data"]['forecast'][0]["ymd"])

