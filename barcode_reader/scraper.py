import requests
import pandas as pd

res = []
url = "https://online.auchan.hu/api/v2/cache/products"
credentials = {
    'usarname':
}
for x in range(2,110):
    querystring = {"page": f"{x}","itemsPerPage":"12","categoryId":"6537","cacheSegmentationCode":"TB_LP0","hl":"hu"}

    payload = ""
    headers = {
        "authority": "online.auchan.hu",
        "accept": "application/json",
        "accept-language": "hu",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4cG1XclQzWmxWMUFJbXdiMUhWYWE5T1BWSzkzcjhIcyIsImp0aSI6ImRlYTQyZGQyNGQ0NDVkYTM0Y2IzMzM2ZDk5YTdlNzg2Y2FlNzU3NDdhODljMDI2YWM5YmU1ZmQ0OGFkNWVlM2NmZDJmOGRlNWYzNzhlM2ExIiwiaWF0IjoxNzA3NTA0OTUyLjY2MjcyOSwibmJmIjoxNzA3NTA0OTUyLjY2MjczNSwiZXhwIjoxNzA3NTkxMzUyLjYzOTI2LCJzdWIiOiJhbm9uX2UwOWE0N2RkLTIwZWUtNGU3Yy1iZTUxLTQ1NTJlMmM4NWU1NCIsInNjb3BlcyI6W119.UsCkiOjhWoN7cxK8on3NE2xwv2mBhbF6eb2-PNUc_JcXQDcnCgUDTI8__jjZV0O83aI_GxIekk8yiJCPzpQg6ggF3hlDqrwL2AOaI9yHqADkdEG4ZW_dNTUs7HfixSOymSuWx8Gztqf_bhSHsqGXUw21BrzEQgq6sbMw-Rres_zhjTNtjZ33liMmtfLHvkvJcV-GsACQpbKTl2kROgY4Uz9YPfVQSPsV91zVyMcx9Qv2GA3ovmvwpK3i3QqrZDSW_Ys5-Nl6qk0nEI5N-WRtMkjsz2XB3VVNooMKnlNq6ltRWWHgwJUep0mDcpO3IeGTJ-PYmDwJHPEFkmxip98LnQ",
        "cookie": "token_type=Bearer; userIsLoggedIn=false; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4cG1XclQzWmxWMUFJbXdiMUhWYWE5T1BWSzkzcjhIcyIsImp0aSI6ImRlYTQyZGQyNGQ0NDVkYTM0Y2IzMzM2ZDk5YTdlNzg2Y2FlNzU3NDdhODljMDI2YWM5YmU1ZmQ0OGFkNWVlM2NmZDJmOGRlNWYzNzhlM2ExIiwiaWF0IjoxNzA3NTA0OTUyLjY2MjcyOSwibmJmIjoxNzA3NTA0OTUyLjY2MjczNSwiZXhwIjoxNzA3NTkxMzUyLjYzOTI2LCJzdWIiOiJhbm9uX2UwOWE0N2RkLTIwZWUtNGU3Yy1iZTUxLTQ1NTJlMmM4NWU1NCIsInNjb3BlcyI6W119.UsCkiOjhWoN7cxK8on3NE2xwv2mBhbF6eb2-PNUc_JcXQDcnCgUDTI8__jjZV0O83aI_GxIekk8yiJCPzpQg6ggF3hlDqrwL2AOaI9yHqADkdEG4ZW_dNTUs7HfixSOymSuWx8Gztqf_bhSHsqGXUw21BrzEQgq6sbMw-Rres_zhjTNtjZ33liMmtfLHvkvJcV-GsACQpbKTl2kROgY4Uz9YPfVQSPsV91zVyMcx9Qv2GA3ovmvwpK3i3QqrZDSW_Ys5-Nl6qk0nEI5N-WRtMkjsz2XB3VVNooMKnlNq6ltRWWHgwJUep0mDcpO3IeGTJ-PYmDwJHPEFkmxip98LnQ; refresh_token=def50200aa81ff0aeea6a788cb2157bba19fbb53c913469545155ea9ca5a15587f8857be801d78967552629e88e5152ce390d84871d449255b587f86caa3691a960e9ba3a84d070b6a4b901e5ffabf4da2aab0bc8861c42a77950e1e1738e415de7448730617fe20b01e87ed7b327dd684d532fffa845691e98bf597a0df65dec0781ea61eb6b965fe8235476adb0326f9bab9e7b15e4f99f0e00be97c34ac92c739e57eb4cea481fd3cb2baa80ecfda9c28063d3596b463136676f30045685e7841502c6401cd777895974cf1099b6c45f5118a294694d1dbe306e505857600c8928c521f44f67a15e3c12f1a429d396c2367a02145313fe8c1c5a297a37083847ee8996e7a81ca9a13bdf39e783776470b1fd3be45b63e23018f7059c78d5bcf1d6be9f66b8cc47166220a74cb62a99102b42fb58d0149024371c2c9c2332a748438afe27c743ca4bdf91310e71d7cbd18e0f65371b137e3d401efccd66a29233cad2a403ab5296a38ece78b298045fd1761d17e8e6e24afb1bbe82c0eaca52eeb48625a8873c18b9d7f9f33fa679422b2acfbdfc3c78612a791b6fa8f2a6d60be986098804ff052c1; isWebpFormatSupportedAlgo0=true; _omappvp=m35L59DqJX3LpAjG1ZB7nTnUdoJjkaYeZb93cb3imRiXj5bnBHUudHjbTHUZ7ZXsrBJMjvECalvOTlasOjaSoFMKh6AcFMg1; _omappvs=1707504954735; scarab.visitor=^%^22E438A1C96DF60B7^%^22; _ga=GA1.2.1374307908.1707504955; _gid=GA1.2.1942556520.1707504955; omSeen-u4iylem6ln5pv81bfbd0=1707504956443; OptanonAlertBoxClosed=2024-02-09T18:55:57.261Z; _gcl_au=1.1.1849657510.1707504957; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+09+2024+19^%^3A55^%^3A57+GMT^%^2B0100+(k^%^C3^%^B6z^%^C3^%^A9p-eur^%^C3^%^B3pai+t^%^C3^%^A9li+id^%^C5^%^91)&version=6.35.0&isIABGlobal=false&hosts=&consentId=28f0626f-1f79-443e-bb40-1447b016daab&interactionCount=1&landingPath=NotLandingPage&groups=C0003^%^3A1^%^2CC0004^%^3A1^%^2CC0002^%^3A1^%^2CC0001^%^3A1; __rtbh.lid=^%^7B^%^22eventType^%^22^%^3A^%^22lid^%^22^%^2C^%^22id^%^22^%^3A^%^22yuMA8RegI4zhpZpU9LLu^%^22^%^7D; _hjSessionUser_606837=eyJpZCI6IjhkMDliMGI5LTdhOGEtNTE3ZC05M2Q0LWQ0ODM4ZDZkZDc4NCIsImNyZWF0ZWQiOjE3MDc1MDQ5NTc0MzUsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_606837=eyJpZCI6IjU0MGVlZmJjLTgxMDEtNDZjMS1iMWY3LWUwZDY2YjdhZjc4OCIsImMiOjE3MDc1MDQ5NTc0MzcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1707504957452.1103446166; tfpsi=2919d951-cd45-4499-a5f1-b8a410dbeae8; _gac_UA-9971642-1=1.1707504975.CjwKCAiAt5euBhB9EiwAdkXWO_9-dhuIztxVyBnS9b7JpTECCE8veEWrYH4lmGZgJMuKk9XG8v1hbxoCq3IQAvD_BwE; _ga_XTT3C4HH22=GS1.2.1707504955.1.1.1707504975.40.0.0; gaHitCounter=5; __rtbh.uid=^%^7B^%^22eventType^%^22^%^3A^%^22uid^%^22^%^2C^%^22id^%^22^%^3A^%^22^%^22^%^7D; om-u4iylem6ln5pv81bfbd0=1707504977774",
        "referer": "https://online.auchan.hu/shop/friss-elelmiszer/tejtermek-tojas-sajt/tejek-tejitalok-novenyi-italok.c-6537",
        "sec-ch-ua": "^\^Not_A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    #access_token_cookie = response.request.headers.get('cookie', '').split('; ')[1].split('=')[1]
    #print(access_token_cookie)

    data = response.json()
    for p in data["results"]:
        res.append(p)
        if data["results"] == None:
            print("this is shit")

print(len(res))
df = pd.json_normalize(res)
df.to_csv('firstresult.csv', encoding='utf-8-sig', index=False)