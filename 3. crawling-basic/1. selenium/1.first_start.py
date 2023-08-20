# pip install selenium
# pip install webdriver_manager
# 크롤링 예제 https://sweetforu.tistory.com/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://moneypin.biz/bizno/")
