import requests
import pandas as pd
from MySql_dumb import *

res = []
url = "https://online.auchan.hu/api/v2/cache/products"
for x in range(1,14):
    querystring = {"page": f"{x}","itemsPerPage":"12","categoryId":"5645","cacheSegmentationCode":"TB_LP0","hl":"hu"}

    payload = ""
    headers = {
        "authority": "online.auchan.hu",
        "accept": "application/json",
        "accept-language": "hu",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4cG1XclQzWmxWMUFJbXdiMUhWYWE5T1BWSzkzcjhIcyIsImp0aSI6IjNhYTViYzVkYjI2M2M0Yzk1MzhjODNmZWRhOGI1MjVlZWZjNTE0MDllNzJlZjY4OWJmM2I4NDA3MDczNzYxZDY5YTgxMjQwNTM2MzgwMmM1IiwiaWF0IjoxNzEwMTc1MjM2LjY1OTQ2MSwibmJmIjoxNzEwMTc1MjM2LjY1OTQ2NiwiZXhwIjoxNzEwMjYxNjM2LjYzNTEzOSwic3ViIjoiYW5vbl84OTA4NjRlMS04ZmVjLTQ0YzktODU2NC04YTg3MTllYmQ1ZGUiLCJzY29wZXMiOltdfQ.Y-E-ozXwbzTlE5ybAkxA83iKnLkp0wMMgcARt7k0MU2tKCxXSwkDrFhpTgx-uZ4tMDnDeGoWucKaWpNs68fmDXsoadMX1xL57rf0asWikYp5QclR5zJwSk5VKYH_tu-pL7JvJM_cOkuuctJkmPI5_CTNcSjhtnkth6GkKs4YzggZ88_Ywrs1IJClJKL1it2p1VDEsyC_IWDAm7W7Gha--mNACl2LkcfO_N5FIv3i9NVWhMky7oH-t96A4i8oJRcVCa17CnxPZpbsmyQbCh0SmY9h3KQDfaCCQQlYpi2EjazVuiRaB7mgexL5XBh_F7DfAY3zHOWw9tEj-VHDzUyVog",
        "cache-control": "no-cache",
        "^cookie": "_omappvp=kPEGKSSbBBJkWJ6VN5ek9rF9E5Jp13fLjQ4PwEdhPsx2bX2pqsNRr68Hr5YTxDJ23FM49H81H6LQEj4CNrdNjagjQF3Az8tL; omSeen-u4iylem6ln5pv81bfbd0=1708094206171; _gcl_au=1.1.1336614653.1708094206; __rtbh.lid=^%^7B^%^22eventType^%^22^%^3A^%^22lid^%^22^%^2C^%^22id^%^22^%^3A^%^22yGOHQHeHvdjZsXJPEUP8^%^22^%^7D; _fbp=fb.1.1708094206350.348490094; _hjSessionUser_606837=eyJpZCI6ImI2ZGNjMzNmLWEyOWYtNTk5MC04N2Y5LWM1MzRjZGY2YmNiZiIsImNyZWF0ZWQiOjE3MDgwOTQyMDYzMjcsImV4aXN0aW5nIjp0cnVlfQ==; OptanonAlertBoxClosed=2024-02-16T16:46:12.490Z; tab-uid_auchanecomm=8a67e872-da6e-4fba-94f7-9ffcdc6f08f0; OptanonAlertBoxClosed=2024-02-20T11:26:50.128Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+20+2024+12^%^3A26^%^3A50+GMT^%^2B0100+(Central+European+Standard+Time)&version=6.38.0&isIABGlobal=false&hosts=&consentId=4638ca5a-b94e-457d-9a0d-da3dc729763c&interactionCount=1&landingPath=NotLandingPage&groups=C0003^%^3A1^%^2CC0004^%^3A1^%^2CC0002^%^3A1^%^2CC0001^%^3A1; _ga=GA1.1.925138390.1708094205; token_type=Bearer; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4cG1XclQzWmxWMUFJbXdiMUhWYWE5T1BWSzkzcjhIcyIsImp0aSI6IjNhYTViYzVkYjI2M2M0Yzk1MzhjODNmZWRhOGI1MjVlZWZjNTE0MDllNzJlZjY4OWJmM2I4NDA3MDczNzYxZDY5YTgxMjQwNTM2MzgwMmM1IiwiaWF0IjoxNzEwMTc1MjM2LjY1OTQ2MSwibmJmIjoxNzEwMTc1MjM2LjY1OTQ2NiwiZXhwIjoxNzEwMjYxNjM2LjYzNTEzOSwic3ViIjoiYW5vbl84OTA4NjRlMS04ZmVjLTQ0YzktODU2NC04YTg3MTllYmQ1ZGUiLCJzY29wZXMiOltdfQ.Y-E-ozXwbzTlE5ybAkxA83iKnLkp0wMMgcARt7k0MU2tKCxXSwkDrFhpTgx-uZ4tMDnDeGoWucKaWpNs68fmDXsoadMX1xL57rf0asWikYp5QclR5zJwSk5VKYH_tu-pL7JvJM_cOkuuctJkmPI5_CTNcSjhtnkth6GkKs4YzggZ88_Ywrs1IJClJKL1it2p1VDEsyC_IWDAm7W7Gha--mNACl2LkcfO_N5FIv3i9NVWhMky7oH-t96A4i8oJRcVCa17CnxPZpbsmyQbCh0SmY9h3KQDfaCCQQlYpi2EjazVuiRaB7mgexL5XBh_F7DfAY3zHOWw9tEj-VHDzUyVog; refresh_token=def5020070ef8b6e58f01738111d933e3b65ca0d437a6b348a9cc8689f2186dfba7decfecb6155c665d74629727ef002386774da0566fe02cd942016f6fa8a3c8641325fcf7aea19a15e91dedc6dc60525c6e2ab7a3203c8a7cb45f1b8d5e34bc99f322adb5fec071a01a9c3a526b7b202625cd6b6a9ce5bc15d31f0fd8f24fea0eaf984aac39814c149831b23f64079c25e0ff6589386ccead0b2b5be0e38fd2a77b0c01ffe153b8aa308ed48af0bc221069012d831f59d2c0239281b9180a60c62f0c8fc58dae9f4e5b2ea9d0d71726f29a320ff1988013c50387004559fdceadd46c1c59be2c1b374f1eb596cf15290878f5fd1554345824ddb3db3236faac9825e35f495ce2e416a55b69214ad096e101191d787319a86fe97d5457b00acc024e63a3584478bb8578468829d32a4cf2d41d9ca3ba3e68bdd2a6b1fab879e16b941351291378de764a209b1c9a433f39a7b7579fb28f5dba6c86da005dbc1af732bd48f5acf99146359eab120701f2d95e2f248f1c72df542cfb68b66edbd3bba946d0b73987387f3dbb5a6b7c176ff5fd598e6e725be59289411e946ec51bfececa32ea1f70e2320; userIsLoggedIn=false; isWebpFormatSupportedAlgo0=true; scarab.visitor=^%^2248B3DFA8C98B2AD0^%^22; _gcl_aw=GCL.1710175240.EAIaIQobChMIioOtm9PshAMVfaiDBx3ECwv3EAAYASAAEgIWmPD_BwE; __rtbh.uid=^%^7B^%^22eventType^%^22^%^3A^%^22uid^%^22^%^2C^%^22id^%^22^%^3A^%^22unknown^%^22^%^7D; _hjSession_606837=eyJpZCI6IjMxYWNiZTEyLWQ2YjAtNDMxNi1hZmU2LWE0MDZlNzNkOTVmZiIsImMiOjE3MTAxNzUyNDAxNjAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+11+2024+17^%^3A40^%^3A40+GMT^%^2B0100+(Central+European+Standard+Time)&version=6.35.0&isIABGlobal=false&hosts=&consentId=4638ca5a-b94e-457d-9a0d-da3dc729763c&interactionCount=1&landingPath=NotLandingPage&groups=C0003^%^3A1^%^2CC0004^%^3A1^%^2CC0002^%^3A1^%^2CC0001^%^3A1; tfpsi=c869b902-02ac-48ea-a0df-23f7d78224ad; omSeen-wuuwcdtznonbrqlbvesb=1710175245785; om-wuuwcdtznonbrqlbvesb=1710175247410; _ga_XTT3C4HH22=GS1.1.1710175239.3.1.1710175250.49.0.0^",
        "pragma": "no-cache",
        "referer": "https://online.auchan.hu/shop/italok/asvanyviz-udito-ital-szorp/szensavas-uditok.c-5645",
        "^sec-ch-ua": "^\^Chromium^^;v=^\^122^^, ^\^Not",
        "sec-ch-ua-mobile": "?0",
        "^sec-ch-ua-platform": "^\^Windows^^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    #access_token_cookie = response.request.headers.get('cookie', '').split('; ')[1].split('=')[1]
    #print(access_token_cookie)

    data = response.json()
    for p in data["results"]:
        categoryName = p.get("categoryName","")
        brandName = p.get("brandName", "")
        productName = p["defaultVariant"].get("name")
        eancode = p["defaultVariant"].get("eanCode")  # Assuming eancode might not always be present
        packageSize = p["defaultVariant"]["packageInfo"].get("packageSize")
        netPrice = p["defaultVariant"]["price"].get("net")
        grossPrice = p["defaultVariant"]["price"].get("gross")
        netDiscountedPrice = p["defaultVariant"]["price"].get("netDiscounted")
        isDiscounted = p["defaultVariant"]["price"].get("isDiscounted")

        mydb = connection_mysql()

        # Check if the eancode already exists in the database
        if not eancode_exists(mydb, eancode):
            commit_mysql(mydb, categoryName,  brandName, productName, eancode, packageSize, netPrice, grossPrice, netDiscountedPrice, isDiscounted)
        if data["results"] == None:
            print("this is shit")

print(len(res))
df = pd.json_normalize(res)
df.to_csv('firstresult.csv', encoding='utf-8-sig', index=False)

