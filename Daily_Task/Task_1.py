'''
Write a script to:
  -> navigate to a Wikipedia
-> Refresh
-> Fetch title
-> Open amazon
-> Fetch title
-> Go back
-> Close
'''
from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.wikipedia.org/")
driver.refresh()
print(driver.title)
sleep(3)
driver.get("https://www.amazon.in/")
sleep(3)
print(driver.title)
driver.back()
sleep(3)
driver.close()