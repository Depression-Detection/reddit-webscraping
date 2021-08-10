# Webdriver Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Misc Imports
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.reddit.com/x")
print(driver.title)
time.sleep(3)
print(driver.current_url)
# driver.close()