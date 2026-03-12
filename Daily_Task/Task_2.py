'''Write a Selenium script to open a website and print the page title.
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Launch Chrome Browser
driver = webdriver.Chrome()

# Open Website
driver.get("https://www.wikipedia.org")

# Wait for page to load
time.sleep(2)

# Print Page Title
print("Page Title is:", driver.title)

# Close Browser
driver.quit()