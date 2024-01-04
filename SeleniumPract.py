from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

#service_obj = Service()
service_obj = Service("F:/pratheep/geckodriver.exe")

driver = webdriver.Firefox(service=service_obj)
"""
driver.get("https://google.com")
driver.maximize_window()
driver.forward()
driver.refresh()
driver.back()
print(driver.title)
print(driver.current_url)
driver.close()
"""
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,".form-control").send_keys("Prt")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("gyyu@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("peyuu")
driver.find_element(By.CLASS_NAME,"form-check-input").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success']").click()
gyu =driver.find_element(By.XPATH,"//div/strong").text
print(gyu)
 
