"""
# Locators - Locators are used to locate the element on the page and perform actions on it.

There are two mwthods to find the elements:
find_element(locator-name,locator-value)
  -> it takes two arguments, this is for single element
  -> Returns a single Web Element object
  ->Finds only the first matching element on the webpage.
  -> if we do not able to find element through it then it gives error/exception "no such element exception"

->find_elements(locator-name,locator-value)
  -> it also take two arguments, this is for multiple elements
  -> return list of web elements
  ->Finds all matching elements on the webpage
  -> if we do not able to find any element then it will return empty list [] ("no error")

locator is address of that particular element
8 types of locator:
DIRECT LOCATOR
->ID
->NAME
->CLASS NAME
->TAG NAME

TEXT BASED
->LINK TEXT
->PARTIAL LINK TEXT

EXPRESSION BASED
->CSS SELECTORS
->XPATH

Element Actions
we can perform many actions but we are learning 2:
-> click ()
to click on the web elements(basic mouse uses)
-> send_keys()
to enter the input in the web

class name and name can be same for multiple so we are going to use xpath

compound class name should be replaced by . in place of space
like the class name is nav-input nav-progressive-attribute so we need to replace space after input with .(dot)
When multiple elements have same class it will take the first element
#Compound class are classes that are nested inside other classes. The compound class name should be replaced with '.'


TAG NAME
# driver.find_element(By.TAG_NAME, "input").send_keys("helloo")
multiple value has same tag name so it gives value to first element having provided tag name
tag name is least used locator


NAME
# driver.find_element(By.NAME, "field-keywords").send_keys("shirts")
# driver.find_element(By.ID, "search").send_keys("shirts")


 CLASS_NAME
# driver.get("https://amazon.com")
# driver.find_element(By.CLASS_NAME, "nav-input.nav-progressive-attribute").send_keys("shirts")


LINK TEXT
Applicable only for anchor tags
for link text and partial link test they are space sensitive as well as case sensitive
driver.get("https://amazon.in/")
# sleep(2)
# driver.find_element(By.LINK_TEXT,"Mobiles").click()


NOTE: id , name , classname and tag name are direct locator whereas link text and  partial link text are text based locators ,and CSS selectors and XPATH are expression based locators


PARTIAL LINK TEXTfor long text it is used
instead of using entire text we can give a part of it
HERE we have freedom of choosing from start or from end or from between
# driver.get("https://amazon.in/")
# sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT, "Mob").click()


CSS SElECTORS - tagname[attribute = "value]
# driver.get("https://amazon.in/")
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"]').send_keys("shirt")

# Another syntax for CSS SELECTORS -> "#" for ID and "." for CLASSNAME
# driver.get("https://demoqa.com/text-box")
# driver.find_element(By.CSS_SELECTOR, "input#userName").send_keys("hahahaha")

syntax is tag_name[attribute ='value ]
ctrl+f in inspect paste tag_name[attribute ='value ] this and check if any area is highlighted if yes then it is present
as expressions are used carefully so it is a way to verify if it is correct or not

We can also provide tag_name[id ="username]=#username  or tag_name#username
for id only # is used
for classname . is used like tag_name[classname="user"] then .user or tag_name .user


XPATH -> XML PATH
-> We can traverse backward or forward
-> Locate elements based on text and attribute
-> These are used for dynamic elements

Is of two types
1. Absolute -> Starts with "/" -> from root
2. Relative -> Starts with "//" -> directly jump to that element

# //tagname[@attribute = "value"]

# driver.get("https://demoqa.com/text-box")
# driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]').send_keys("hehehehe")
# driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

# If we want to find by some part of attribute value
# We can give full or partial value of attribute's value
# driver.get("https://amazon.in/")
# sleep(4)
# driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search Amazon')]").send_keys("Shirt")

# If we want to find by some part of text or full text
driver.get("https://amazon.in/")
sleep(4)

# Using text - text() ->
# driver.find_element(By.XPATH,'//a[contains(text(),"Mobiles")]').click()

# Another syntax - "."
# driver.find_element(By.XPATH,'//a[contains(.,"Mobiles")]').click()

# We can also find element using XPATH using indexing
driver.find_element(By.XPATH, '//li[@class="navFooterDescItem"][2]').click()
"""


""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
"""

# 1. ID locator
#send_keys() and click() element method
# it is used to locate the element by its unique id
# fastest, primarily and most priority

#enter values in Demoqa website and click on submit
"""
driver.find_element(By.ID,"userName").send_keys("Nehal Agarwal")
driver.find_element(By.ID,"userEmail").send_keys("nehala1801@gmail.com")
driver.find_element(By.ID,"currentAddress").send_keys("JECRC university, Jaipur")
driver.find_element(By.ID,"permanentAddress").send_keys("Ajmer")
driver.find_element(By.ID,"submit").click()   #the click method is used to click on element and return type is None
sleep(2)
driver.close()
"""

# example - locate the search bar for amazon website
"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Shirts")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.close()
"""


# 2. NAME locator
#it is used to locate the element by its unique name
""" 
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.NAME,"field-keywords").send_keys("Shirts")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.close()
"""

# 3. CLASS_NAME locator
#it is used to locate the element by its unique class name
""" from selenium.webdriver import Chrome,ChromeOptions 
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
#Compound class are classes that are nested inside other classes. The compound class name should be replaced with '.'. 
driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("Shirts") 
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
driver.close()
"""

# 4. TAG_NAME locator(least used)
#it is used to locate the element by its unique tag name
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.TAG_NAME,"input").send_keys("Anushka") #enters the value in first input field
driver.find_element(By.TAG_NAME,"input").send_keys("anushka@gmail.com") #enters the value in first input field only because its retrieving the first input field
driver.find_element(By.TAG_NAME,"textarea").send_keys("Jaipur") #enters the value in first text area
driver.find_element(By.TAG_NAME,"textarea").send_keys("city")
sleep(5)
driver.close() 
"""

# 5. LINK_TEXT locator(works for only anchor tags)
#It is case sensitive and space sensitive
#it is used to locate the element by its unique link text, used only for anchor tags
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.LINK_TEXT,"Today's Deals").click() #take the visible text of the element and click on it
sleep(5)
driver.close() """

# 6. PARTIAL_LINK_TEXT locator(works for only anchor tags)
#it is used to locate the element by its unique partial link text, used only for anchor tags
# difference between link text and partial link text is that link text is used to locate the element by its complete link text, while partial link text is used to locate the element by its partial link text only
# link text and partial link text are space and case sensitive
""" from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.PARTIAL_LINK_TEXT,"Today").click() #take the visible text of the element and click on it
sleep(5)
driver.close()
"""

# 7. CSS_SELECTOR locator
#it is used to locate the element by its unique CSS Selector
"""
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
#locating the search bar for amazon website
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox").send_keys("Skirts") #here #twotabsearchtextbox is the css selector which is used to locate the search bar
driver.find_element(By.CSS_SELECTOR,"#nav-search-submit-button").click()
sleep(5)
driver.close()
"""

# by class name
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
#locating the Full Name text box by its class name with help of CSS Selector
driver.find_element(By.CSS_SELECTOR,".mr-sm-2.form-control").send_keys("Anushka") #enters the value in first input field
sleep(5)
driver.close()