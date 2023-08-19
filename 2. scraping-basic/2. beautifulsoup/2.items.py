import requests
from bs4 import BeautifulSoup

print("파이썬 웹 크롤링")

r = requests.get("https://pcm9881.tistory.com/")

html = r.text

soup = BeautifulSoup(html, "html.parser")

post_items = soup.select("#content > div.inner > .post-item")  # CSS Selector

post_len = len(post_items)

print(f"포스트 수: {post_len}")

for post in post_items:
    title_tag = post.find("span", "title")
    print(title_tag.text)
