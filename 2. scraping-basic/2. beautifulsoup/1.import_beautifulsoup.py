# pip install requests

import requests
from bs4 import BeautifulSoup

print("파이썬 웹 크롤링")

r = requests.get("https://pcm9881.tistory.com/")

html = r.text

# BeautifulSoup은 HTML을 읽어서 쉽게 파싱(pasing)을 지원해주는 라이브러리입니다.
# 기본 설치시 html.parser를 제공하지만 추가적으로 원하는 파싱 라이브러리를 설치해서 사용 할 수 있습니다.
# 파싱 (pasing): 구문분석
soup = BeautifulSoup(html, "html.parser")

select_html = soup.select("#header > div > h1 > a")  # CSS Selector

print(select_html)

print(select_html[0].text)

print(
    select_html[0].text.strip()
)  # 공백제거 text.lstrip() : 왼쪽 text.rstrip() : 오른쪽 text.strip() : 양쪽
