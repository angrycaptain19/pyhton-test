from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    order = (By.ID, "sort")
    price = (By.CSS_SELECTOR, "span[class='price']")

    def getSortPrices(self):
        return self.driver.find_element(*ResultPage.order)

    def getFlightPrices(self):
        return self.driver.find_elements(*ResultPage.price)
