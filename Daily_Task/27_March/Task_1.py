from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.implicitly_wait(10)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"ico-register").click()
sleep(2)
def test_gender():
    driver.find_element(By.ID,"gender-male").click()
    sleep(2)
def test_name():
    driver.find_element(By.ID,"FirstName").send_keys("Yash")
    sleep(2)
def test_Lname():
    driver.find_element(By.ID,"LastName").send_keys("Rathore")
    sleep(2)
def test_mail():
    driver.find_element(By.ID,"Email").send_keys("yash@gmail.com")
    sleep(2)
def test_pass():
    driver.find_element(By.ID,"Password").send_keys("test@123")
    sleep(2)
def test_cpass():
    driver.find_element(By.ID,"ConfirmPassword").send_keys("test@123")
    sleep(2)
def test_button():
    driver.find_element(By.ID,"register-button").click()
    sleep(5)