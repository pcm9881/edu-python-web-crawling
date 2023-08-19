# pip install requests

import requests

print("파이썬 웹 크롤링")

r = requests.get("https://pcm9881.tistory.com/")

print(r.text)  # HTML

print(r.status_code)  # HTTP Status Code

print(r.headers)  # 요청 Headers

print(r.ok)  # HTTP 정상동작 여부
