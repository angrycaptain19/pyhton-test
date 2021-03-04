class ResultPage:
    def __init__(self, driver):
        self.driver = driver


    order = (By.ID, "sort")


    def getSortPrices(self):
        return self.driver.find_element(*ResultPage.order, "desc")