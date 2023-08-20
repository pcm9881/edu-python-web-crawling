from time import sleep
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

enter_action = (
    webdriver.ActionChains(driver)
    .send_keys_to_element(biz_input, "중공업")
    .send_keys(Keys.ENTER)
)
enter_action.perform()

sleep(2)  # 프로세스는 유지되지만 2초동안 잠시 멈추게 됩니다.

section_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > div > section")

a_tag_elements = section_element.find_elements(By.CSS_SELECTOR, "a")

for a_tag in a_tag_elements:
    a_tag.click()  # 클릭은 요소(element)를 찾으면 매우 쉽게 할 수 있습니다.
    break
