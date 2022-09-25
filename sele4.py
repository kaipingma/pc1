from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


# TODO
# 1. Use the latest webdriver syntax
# 2. Use the latest find element function

page = 'https://wiki.python.org/moin/FrontPage'
chrome = 'drivers/chromedriver'
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
