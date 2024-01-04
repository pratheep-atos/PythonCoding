from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")

    def shop_items(self):
        self.driver.findElement(*HomePage.shop).click()



