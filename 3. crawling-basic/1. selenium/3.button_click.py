from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
actions = (
    webdriver.ActionChains(driver)
    .send_keys_to_element(biz_input, "중공업")
    .send_keys(Keys.ENTER)
)
actions.perform()
