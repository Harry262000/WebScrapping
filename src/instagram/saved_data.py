from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Instagram login page
driver.get("http://www.instagram.com")

# Target Username and Password fields
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Enter the username and password
username.clear()
username.send_keys("Hondeharshal22@gmail.com")
password.clear()
password.send_keys("")  

# Target the login button and click it
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()

# Wait for 2FA code entry
print("Please enter the 2FA code manually on the Instagram website...")

# Pause script execution to allow for manual 2FA code entry
time.sleep(90)  

# Handle "Not Now" button for saving login info
try:
    not_now_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))
    )
    not_now_button.click()
except:
    print("No 'Not Now' button found, continuing...")

# Continue with additional actions after 2FA
driver.get("https://www.instagram.com/harshaalmarshaal/saved/all-posts/")
time.sleep(45) 

# Scrape saved posts
posts = driver.find_elements(By.XPATH, '//article//img')
for post in posts:
    src = post.get_attribute('src')
    print(src) 

# Close the browser
driver.quit()
