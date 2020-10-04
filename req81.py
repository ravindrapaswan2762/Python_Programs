
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.text)
print(r.status_code)



"""url = "http://www.newsapi.org"

data = {
     "user name":4,
     "password":8
 }
r2 = requests.post(url=url, data=data)
print(r2.text)"""

######## OR #########
"""payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()
print(r_dict['form'])"""
#######################################################
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
print(r)





