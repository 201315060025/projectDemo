import requests,json

# requests.post(url='http://localhost:5000/create-stage', data={"name": "blx"})

# requests.get(url='http://localhost:5000/get-stage? id=123')

res = requests.post(url='http://localhost:8000/get-option')
print(res.text)