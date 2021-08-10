# Webdriver Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Misc Imports
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
print(driver.current_url)
driver.close()