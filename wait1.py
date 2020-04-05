from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome = '/Users/kaipingma/play/notebook/chromedriver'
driver = webdriver.Chrome(chrome)
driver.get('http://www.python.org')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "start-shell"))
        )
    time.sleep(5)
    element.click()
    time.sleep(10)
finally:
    driver.quit()
