import requests

url_post = 'http://127.0.0.1:5000/get_user/'

data = {'username': 'km'}

r = requests.get(url_post, data)
print(r.url)
print(r.status_code)
