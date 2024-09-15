import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
driver = webdriver.Chrome(options)

for x in range(1,3):
    url = f'https://english.onlinekhabar.com/category/political/page/{x}'
    driver.get(url)
    elementToWait = WebDriverWait(driver,3).until(
        EC.presence_of_element_located ((By.CLASS_NAME, 'listical-news-big'))
    )
    mainElement = driver.find_element(By.CLASS_NAME, 'listical-news-big')
    newsHeadingClass = mainElement.find_elements(By.CLASS_NAME,'ok-post-contents')
    for heading in newsHeadingClass:
        headingText = heading.text.split("\n")[0]
        print(headingText)

#titleElement = driver.find_element (By.CLASS_NAME,'ok-inner-page-title')
#print(titleElement.text)
#time.sleep(5)

