from selenium import webdriver
import time


CHRM = '/Users/kaipingma/play/notebook/chromedriver'
driver = webdriver.Chrome(CHRM)
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('driver started.')

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

print("driver to sleep 10s.")
time.sleep(10)

driver.quit()
print("driver quited.")
