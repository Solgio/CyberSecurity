#import string
#import requests
#
#for i in string.ascii_letters:
#    url = f"http://127.0.0.1:124/?pass={i}"
#    r = requests.get(url, headers={'User-Agent': str(i)})
#    print(r.text)
#
# '{"cookies": {"sessioncookie": "123456789"}}'


from hashlib import md5
import string
import requests

for i in range(0,100):
    
    giorgio=md5(b'{i}')
    url = f"http://127.0.0.1:8080/"
    r = requests.get(url, '{"cookies": {"UID": "{giorgio}"}}')
    print(r.text)
