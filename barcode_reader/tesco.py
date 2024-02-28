import pandas as pd
import requests

res = []
url = "https://shopservice.roksh.com/productlist/CategoryProductList"

querystring = {"progId":"zoldseg-gyumolcs","firstLoadProductListResultNum":"4","listResultProductNum":"24"}

payload = ""
headers = {
    "cookie": "ARRAffinity=c61624bc096e943b61cd8e33c9609c065f97d78b2451ec8856a67e60445a4578; ARRAffinitySameSite=c61624bc096e943b61cd8e33c9609c065f97d78b2451ec8856a67e60445a4578",
    "authority": "shopservice.roksh.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiNjEzNGExZDBiMGY1NGFlOTg2Njk1ZDI1NGJiZTA5YTQiLCJleHAiOjE3MTAwMjM3NTQsImlzcyI6IldFU0hPUEFQSSIsImF1ZCI6IldlU2hvcEF1ZGllbmNlIn0.QfcUrsqZj4yEQz9npC2kwtWR9Murvr1Sattr8EgYvcM",
    "cache-control": "no-cache",
    "origin": "https://shop.aldi.hu",
    "pragma": "no-cache",
    "referer": "https://shop.aldi.hu/",
    "sec-ch-ua": "^\^Not",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

data = response.json()
print(data.keys())
for p in data["SubCategories"]:
    res.append(p["ParentCategory"])
print(res)
df = pd.json_normalize(res)
df.to_csv('aldiresult.csv', encoding='utf-8-sig', index=False)
