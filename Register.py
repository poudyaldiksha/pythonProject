import time

from scipy.constants import value
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
driver = webdriver.Chrome(options)

#Open url and maximize window
driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
driver.maximize_window()

#Enter the username
username= driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys("poudyald553@gmail.com")
time.sleep(1)

username= driver.find_element(By.XPATH, '//*[@id="password"]')
username.send_keys("Tolphin5%")
time.sleep(1)
import time

from scipy.constants import value
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
driver = webdriver.Chrome(options)

#Open url and maximize window
driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
driver.maximize_window()

#Enter the username
username= driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys("poudyald553@gmail.com")
time.sleep(1)

username= driver.find_element(By.XPATH, '//*[@id="password"]')
username.send_keys("Tolphin5%")
time.sleep(1)

sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
sign_in_button.click()

time.sleep(3)

driver.get("https://www.linkedin.com/feed/")

driver.quit()






















