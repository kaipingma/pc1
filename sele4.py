from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

chrome = '/Users/kaipingma/play/notebook/chromedriver'
page = 'https://wiki.python.org/moin/FrontPage'

driver = webdriver.Chrome(chrome)
driver.get(page)
time.sleep(2)

search = driver.find_element_by_id('searchinput')
search.clear()
search.send_keys('Beginner')
search.send_keys(Keys.RETURN)
time.sleep(2)

select = Select(driver.find_element_by_xpath('//select'))
select.select_by_value('raw')
time.sleep(2)

driver.quit()
