from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


# Initialize the WebDriver
driver = webdriver.brave()

# open the webdriver

driver.get("http://www.google.com")

time.sleep(40)

driver.quit()