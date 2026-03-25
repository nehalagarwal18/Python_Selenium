""" Task-4: open internent.herokuapp.com
open JS alerts
practice on all three alerts and also print the text from the alert """

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert1=driver.switch_to.alert
print(alert1.text)
alert1.accept()
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert2=driver.switch_to.alert
print(alert2.text)
alert2.accept()
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert3=driver.switch_to.alert
print(alert3.text)
alert3.send_keys("Nehal Agarwal")
alert3.accept()
sleep(5)