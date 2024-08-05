from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Function to simulate human-like scrolling
def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Twitter login page
driver.get("https://twitter.com/login")
time.sleep(10)  # Adjust time as needed

# Log in to Twitter
username = driver.find_element(By.NAME, "session[username_or_email]")
password = driver.find_element(By.NAME, "session[password]")
username.send_keys("hondeharshal22@gmail.com")  # Replace with your Twitter username
password.send_keys("Saved3-Gullible1-Retaliate9-Persuader1-Smashing9")  # Replace with your Twitter password
password.send_keys(Keys.RETURN)
time.sleep(10)  # Adjust time as needed

# Navigate to the desired Twitter page
driver.get("https://x.com/search?vertical=trends&q=lang%3Ahi%20until%3A2024-07-31%20since%3A2024-01-01%20-filter%3Alinks&src=typed_query")  # Replace 'your_query' with your search query
time.sleep(8)  # Adjust time as needed

# Simulate human-like scrolling and scraping tweets
tweets_data = []
scroll_pause_time = random.uniform(1, 3)  # Random delay between scrolls

start_time = time.time()
end_time = start_time + 1000  # Run for 1 hour

while time.time() < end_time:
    scroll_down(driver, scroll_pause_time)
    tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

    for tweet in tweets:
        try:
            tweet_text = tweet.find_element(By.XPATH, ".//div[2]/div[2]/div[1]").text
            tweets_data.append(tweet_text)
        except Exception as e:
            print(e)
    
    time.sleep(random.uniform(1, 3))  # Random delay between actions

# Close the driver
driver.quit()

# Output scraped data
for tweet in tweets_data:
    print(tweet)
