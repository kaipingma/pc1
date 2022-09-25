from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# chrome = 'drivers/chromedriver'
# driver = webdriver.Chrome(chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('driver started.')

element1 = driver.find_element(By.ID, 'navbar')
print(element1)
# messageField = driver.find_element(By.XPATH, '//*[@id="user-message"]')
# messageField.send_keys('Hello World')
# showMessageButton = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
# showMessageButton.click()

print("driver to sleep 10s.")
time.sleep(10)

driver.quit()
print("driver quited.")
