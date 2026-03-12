'''Write a Selenium script to open a website and print the current URL.
'''
from selenium import webdriver
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.wikipedia.org")

# Wait for page to load
time.sleep(2)

# Print current URL
print("Current URL is:", driver.current_url)

# Close browser
driver.quit()