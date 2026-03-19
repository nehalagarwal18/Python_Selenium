"""
install PyCharm
then in pycharm terminal install selenium :
pip install selenium


1->launch the browser
make a launch.py file
in launch.py file
from selenium.webdriver import Chrome
//from selenium package in webdriver module we are importing class Chrome
driver =Chrome()
driver is a var which is holding the browser
//driver is the variable that is holding the chrome
// after this there is a blink of white screen
// to stop white screen for more time we can use sleep(time)
sleep is not a standard way to hold the browser
"""


#Opening Chrome browser/ to launch chrome
""" from time import sleep
from selenium.webdriver import Chrome
driver = Chrome()
sleep(5) """

#Opening edge browser
""" from time import sleep
from selenium.webdriver import Edge
driver = Edge()
sleep(5)
#not the standard way 
"""

#Opening Chrome browser and keeping it open after execution
""" 
to hold the browser by change in Chrome options
these are extra browser settings to hold the window
to keep the browser open after execution 

from selenium.webdriver import Chrome,ChromeOptions  #importing the class Chrome and ChromeOptions from the selenium.webdriver module
o = ChromeOptions()  #creating an object of the class ChromeOptions and storing it in the variable o
o.add_experimental_option("detach",True)   #adding an experimental option to the ChromeOptions object to keep the browser open after the script is executed
this will hold the window if we pass false then again it will blink
in this add_experimental_option is just a browser setting that we are doing to hold the browser 

driver = Chrome(options=o) 
#driver is the object of the class Chrome and we are passing the options to it
#driver is the object holding Chrome browser 
if we do not pass options=o then also browser will blink

#to open websites
driver.get("https://www.google.com/") 
return type of get() is None
we need to pass a url inside get() method
get() method will open the usl passed in it

# Browser window management methods

#to maximize the browser window
driver.maximize_window() 
maximizing the browser window using the maximize_window method of the driver objects
return type is None

#to minimize the browser window
driver.minimize_window() 
minimizing the browser window using the minimize_window method of the driver object
return type is None

#to set full screen
driver.fullscreen_window() 
setting the browser window to full screen using the fullscreen_window method of the driver object
return type is None
we will not be using this
while using this task bar and title bar will not shown

for printing link of the website in terminal
these are the page info properties 
# print(driver.current_url)
# print(driver.page_source)

to print the name of the browser
print(driver.name)
fetching the name of the browser using the name attribute of the driver object
return type is str
"""

# selenium is acting fast whereas browser is not so to solve this we will use sleep and wake in between

#To open amazon.com and do min max and fullscreen
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.com/")
sleep(2)
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()
to do all 3 task together we will use sleep() between all 3 as selenium is very fast and browser is slow so to match both we use sleep and wake

#Page information properties

//Fetch the title of the page
print(driver.title) 
etching the title of the current page using the title attribute of the driver object
we fetch title to perform validation
return type is string
title is not a method it is a verification property
t = driver.title       
print(t)

#to fetch the current url of the page
print(driver.current_url) 
etching the current url of the page using the current_url attribute of the driver object
return type is string
sometimes title are same for multiple sites so we use current_url for verification

#to fetch the page source of the page
print(driver.page_source) 
fetching the page source of the current page using the page_source attribute of the driver object
It is not used much,gives html file
return type is string """

# note: maximize_window , minimize_window and fullscreen_window are window size method
# note: title , current_url and page_source are page information properties or verification properties not method

#to close the browser(only the current tab)
""" driver.close() 
return type is None
Suppose we open more tab manually in browser then this will close the url tab only as the sleep time completes
close is going close only the tab we are fetching , it don't effect any other tab """

#to quit the browser(all the tabs)
""" driver.quit() 
return type is None
Suppose we open more tab manually in browser then this will close all tabs including url page as the sleep time completes
close all the tabs and exit from the browser"""

# NOTE-- for single tab both close() and quit() will perform same
# NOTE-- but for many tabs close() will close only the tab that driver is carrying whereas quit will close the whole browser means all tabs get closed

# whenever we launch we have 3 options back , next and refresh so to do that we have 3 methods:
# driver.back()
# driver.forward()
# driver.refresh()

# to open demoqa.com
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/")
print(driver.title)
print(driver.current_url)
sleep(2)

#return name of browser
print(driver.name) 
fetching the name of the browser using the name attribute of the driver object
print the name of the browser we are using
return type is string """


#to navigate to a new url
"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.com/")
driver.maximize_window()
sleep(4)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.close()
"""

#open wikipedia , refresh , fetch the title  , open amazon , fetch title, go back , go close
"""driver.get("https://www.wikipedia.org/")
sleep(5)
driver.refresh()
sleep(5)
print(driver.title)
driver.get("https://www.amazon.com/")
sleep(5)
driver.refresh()
print(driver.title)
sleep(5)
driver.back()
sleep(5)
driver.close()
"""

