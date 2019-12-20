from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("w3schools")
driver.find_element_by_name("btnk").sen_keys(Keys.ENTER)
time.sleep(2)
driver.quit()
