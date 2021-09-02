import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, executable_path="../driver/geckodriver" )

driver = webdriver.Firefox()

driver.get("https://www.google.com")

print("Before Title :==", driver.title)


driver.set_page_load_timeout(3)

driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.set_page_load_timeout(3)

print("After Title :==  ", driver.title)



#driver.find_element_by_name("btnK").click()

time.sleep(2)
driver.close()
driver.quit()
