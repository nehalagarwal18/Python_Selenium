
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Nehal Agarwal")


driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, '//input[@placeholder="name@example.com"]').send_keys("nehala1801@gmail.com")
sleep(2)


driver.get('https://amazon.com/')
sleep(5)
driver.find_element(By.XPATH, '(//span[@class="navFooterDescText"])[9]').click()