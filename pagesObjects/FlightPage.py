from selenium.webdriver.common.by import By



class FlightPage:
    def __init__(self, driver):
        self.driver = driver



    origin = (By.ID, "flight-from")
    destination = (By.ID, "flight-to")
    departing_date = (By.ID, "departing")
    returning_date = (By.ID, "returning")
    search_btn = (By.XPATH, "//button[@class='btn btn-primary button-ns']")

    def getOrigin(self):
        return self.driver.find_element(*FlightPage.origin)

    def getDestination(self):
        return self.driver.find_element(*FlightPage.destination)

    def getDepartingDate(self):
        return self.driver.find_element(*FlightPage.departing_date)

    def getReturninDate(self):
        return self.driver.find_element(*FlightPage.returning_date)

    def search(self):
        return self.driver.find_element(*FlightPage.search_btn).click()
