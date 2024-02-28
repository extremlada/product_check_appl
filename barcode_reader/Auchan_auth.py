import requests
auth_url = "https://online.auchan.hu/login"
credentials = {
    'email': 'becsfenc@gmail.com',
    'password': 'AsdAsd123'
}

response = requests.post(auth_url, json=credentials)

print(response.text)

if response.status_code == 200:
    jwt_token = response.json().get('jwt_token')
    print(jwt_token)
else:
    print("Auth failed", response.text)