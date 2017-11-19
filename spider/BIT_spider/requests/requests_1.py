import requests

r = requests.get("http://www.baidu.com")
print(r.status_code)

print(type(r))

print(r.headers)
