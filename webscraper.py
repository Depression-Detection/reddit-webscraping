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

no_of_pagedowns = 20
subreddit_data = []
for username in df[0]:
    driver.get("https://www.reddit.com/user/" + username)

    while no_of_pagedowns:
        driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    a = driver.find_elements_by_class_name("_3ryJoIoycVkA88fy40qNJc")
    subreddit_data.append([subreddit.text for subreddit in a])
driver.close()
print(subreddit_data)
