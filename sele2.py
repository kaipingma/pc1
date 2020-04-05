from selenium import webdriver
import time


CHRM = '/Users/kaipingma/play/notebook/chromedriver'
driver = webdriver.Chrome(CHRM)
driver.get('http://www.seleniumhq.org/')
print('driver started.')

element1 = driver.find_element_by_id('gsc-i-id1')
print(element1)

element2 = driver.find_element_by_name('search')
print(element2)

element3 = driver.find_element_by_xpath('//*[@id="gsc-i-id1"]')
print(element3)

print("driver to sleep 10s.")
time.sleep(10)

driver.quit()
print("driver quited.")
