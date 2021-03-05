from datetime import datetime, timedelta

from selenium.webdriver.common.by import By
from pagesObjects.FlightPage import FlightPage


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    today_date = datetime.today()
    new_today_date = today_date.strftime("%d/%m/%Y")
    next_date = (today_date + timedelta(10)).strftime("%d/%m/%Y")

    flight = (By.LINK_TEXT, "Flights")

    def goToFlights(self):
        self.driver.find_element(*BasePage.flight).click()
        return FlightPage(self.driver)
