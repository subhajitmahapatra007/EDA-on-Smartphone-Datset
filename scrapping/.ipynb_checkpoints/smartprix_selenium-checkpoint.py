import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.smartprix.com/mobiles")
    wait.until(EC.url_contains("https://www.smartprix.com/mobiles"))

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span').click()

    wait.until(EC.url_contains("https://www.smartprix.com/mobiles/exclude_out_of_stock-exclude_upcoming-stock"))

    old_height = driver.execute_script('return document.body.scrollHeight')

    while True:
        driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div/div[3]').click()
        time.sleep(3)

        new_height = driver.execute_script('return document.body.scrollHeight')

        print(old_height)
        print(new_height)

        if new_height == old_height:
            break

        old_height = new_height

    html = driver.page_source

    with open('smartprix2.html', 'w', encoding='utf-8') as f:
        f.write(html)

except Exception as e:
    print(e)
