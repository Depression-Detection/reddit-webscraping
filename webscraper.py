# Webdriver/Webscraper Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Misc Imports
import time

# Data Processing Imports
import pandas as pd

df = pd.read_csv("users.csv", header=None) 
driver = webdriver.Chrome(ChromeDriverManager().install())

for username in df[0]:
    driver.get("https://www.reddit.com/user/" + username)
driver.close()