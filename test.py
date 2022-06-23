import time
import requests

res=requests.get('https://afdian.net/@oysuminasai')
print(res.text)