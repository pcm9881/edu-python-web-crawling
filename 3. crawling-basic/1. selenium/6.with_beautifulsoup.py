from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.implicitly_wait(3)

driver.get("https://moneypin.biz/bizno/")

biz_input = driver.find_element(
    By.CSS_SELECTOR,
    "#__next > main > div > form > div.mt-6.lg\:w-full.lg\:mt-9 > div",
)

enter_action = (
    webdriver.ActionChains(driver)
    .send_keys_to_element(biz_input, "중공업")
    .send_keys(Keys.ENTER)
)
enter_action.perform()

sleep(2)  # 프로세스는 유지되지만 2초동안 잠시 멈추게 됩니다.

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

sections = soup.select("#__next > main > div > section > a")

companies = []

for section in sections:
    # saction
    id = section.get("id")

    # 1개 아이템 클릭
    driver.find_element(By.ID, id).click()

    sleep(1)

    content_soup = BeautifulSoup(driver.page_source, "html.parser")

    company = {}
    company["ceo"] = content_soup.select_one("#ceo").text
    company["businessNumber"] = content_soup.select_one(
        "#__next > main > div > div > section > div:nth-child(2) > div.mx-auto.lg\:my-0.w-full.lg\:w-\[768px\] > div.px-6.pt-8.lg\:pt-14.lg\:px-0 > ul > li:nth-child(2) > p.w-3\/5.lg\:text-lg"
    ).text

    companies.append(company)
    break

print(companies)
