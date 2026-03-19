""" Task-2: Open Demoqa
add your details in the webtables
fetch your name and salary
and print 'name=salary' """

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id = 'addNewRecordButton']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Nehal")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Agarwal")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("nehal123@gmail.com")
driver.find_element(By.XPATH, "//input[@id='age']").send_keys("22")
driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("100000")
driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Q&T")
driver.find_element(By.XPATH, "//button[@id = 'submit']").click()

salary = driver.find_element(By.XPATH, "//td[text() = 'Nehal']/..//td[5]")
print("The Salary is:",salary.text)

driver.quit()