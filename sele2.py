from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# chrome = 'drivers/chromedriver'
# driver = webdriver.Chrome(chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://www.seleniumhq.org/')
print('driver started.')

element1 = driver.find_element(By.ID, 'main_navbar')
print(element1)

# element2 = driver.find_element(By.NAME, 'Search')
# print(element2)

element3 = driver.find_element(By.XPATH, '//*[@id="main_navbar"]')
print(element3)

print("driver to sleep 10s.")
time.sleep(10)

driver.quit()
print("driver quited.")
