from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://amazon.in/")
#return type none
# driver.maximize_window()
#return type none

# driver.fullscreen_window()
# sleep(5)

#to fetch the title
title = driver.title
print(title)

print(driver.current_url)
print(driver.page_source)
driver.refresh()
driver.forward()
driver.back()
sleep(7)


name = driver.name
print(name)


# driver.close()
# driver.quit()

'''
from selenium.webdriver import Chrome,ChromeOptions --> from this we are importing moduls of selenium.webdriver 
driver is a var which is holding the browser
o.add_experimental_option("detach", False) --> in this add_experimental_option is just a browser setting that we are doing to hold the browser 

these are browser window size methods 
driver.maximize_window()
driver.fullscreen_window()

these are the page info properties 
print(driver.current_url)
print(driver.page_source)

driver.close()--> close is going close only the tab we are fetching , it don't effect any other tab 
driver.quit()--> close all the tabs and exit from the browser

'''