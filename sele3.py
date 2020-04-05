from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

chrome = '/Users/kaipingma/play/notebook/chromedriver'
page = 'file:///Users/kaipingma/play/Linkedin_Python_Automation_Testing/Exercise%20Files/CH03/03_02/html_code_03_02' \
       '.html'

driver = webdriver.Chrome(chrome)
driver.get(page)
time.sleep(2)

select = Select(driver.find_element_by_name('numReturnSelect'))
select.select_by_index(1)
time.sleep(2)
select.select_by_visible_text("800")
time.sleep(2)
select.select_by_value("15000")
time.sleep(2)

options = select.options
print(options)

submit_button = driver.find_element_by_name('continue')
submit_button.submit()
time.sleep(2)

driver.quit()
