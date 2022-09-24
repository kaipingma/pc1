from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome = 'drivers/chromedriver'
driver = webdriver.Chrome(chrome)
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('driver started.')

messageField = driver.find_element(By.XPATH, '//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
showMessageButton.click()

print("driver to sleep 10s.")
time.sleep(10)

driver.quit()
print("driver quited.")
