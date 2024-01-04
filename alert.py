from selenium.webdriver.common.by import By

from SeleniumPract import driver



driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("pratheep")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()

alertInfo =driver.switch_to.alert
alertInfo.accept()
