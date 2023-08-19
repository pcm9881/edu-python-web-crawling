import requests
from bs4 import BeautifulSoup

print("파이썬 웹 크롤링")

r = requests.get("https://pcm9881.tistory.com/")

html = r.text

soup = BeautifulSoup(html, "html.parser")

pagination = soup.select("#content > div.pagination > a")  # pagination

# 현재 페이지가 여러개 존재하는지 확인
page_len = len(pagination)

# 페이지가 한개만 있는 경우 예시: https://penguin5.tistory.com/category/Investing

print(f"페이지: {page_len}")

last_child = soup.select("#content > div.pagination > a:last-child")

print(last_child)

nth_last_child_1 = soup.select("#content > div.pagination > a:nth-last-child(1)")

print(nth_last_child_1)

nth_last_child_2 = soup.select("#content > div.pagination > a:nth-last-child(2)")

last_page = int(nth_last_child_2[0].text)  # 마지막 페이지


post_items = soup.select("#content > div.inner > .post-item")  # CSS Selector

post_len = len(post_items)

print(f"포스트 수: {post_len}")

titles = []

for post in post_items:
    title_tag = post.find("span", "title")
    print(title_tag.text)
    titles.append(title_tag.text)


if page_len > 1:
    for i in range(2, last_page + 1):
        r = requests.get(f"https://pcm9881.tistory.com/?page={i}")

        html = r.text

        soup = BeautifulSoup(html, "html.parser")

        post_items = soup.select("#content > div.inner > .post-item")  # CSS Selector

        post_len = len(post_items)

        print(f"포스트 수: {post_len}")

        for post in post_items:
            title_tag = post.find("span", "title")
            print(title_tag.text)
            titles.append(title_tag.text)


print(len(titles))  # 150
