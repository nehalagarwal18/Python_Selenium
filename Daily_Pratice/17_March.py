# Implicit wait
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.TAG_NAME,"button").click()
driver.implicitly_wait(20)
t = driver.find_element(By.XPATH,"//div[@id='finish']//h4")
print(t.text) # won't print anything as the element is not visible
driver.close() """

# 2
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://www.decathlon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//img[@src='https://contents.mediadecathlon.com/s1371134/k$314e5f23e193aab04dceff5d9bcbdee4/defaut.jpg?format=auto&quality=70&f=2520x0']").click()
driver.find_element(By.XPATH,"//img[@alt='Beanies & Neck Warmers']").click()
driver.close() """

# Explicit wait
""" from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #alias name
o = ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.find_element(By.TAG_NAME,"button").click()
wait = WebDriverWait(driver,20) #wait object
t = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']//h4"))) #expected conditions
print(t.text)
driver.close() """

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[text()='Start']").click()
# t=driver.find_element(By.XPATH,"//button[text()='Start']")
# driver.implicitly_wait(10)
# print(t.text)


# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://www.decathlon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/shop/Winter-Collection']").click()
# driver.implicitly_wait(10)


'''
from asyncio import timeout
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
sleep(2)
driver.maximize_window()
sleep(2)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[text()='Start']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']")))
ans=driver.find_element(By.XPATH,"//div[@id='finish']")
print(ans.text)
'''
