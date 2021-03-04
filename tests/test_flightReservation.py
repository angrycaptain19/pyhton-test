from pagesObjects.BasePage import BasePage
from pagesObjects.ResultPage import ResultPage
from utlilities.BaseClass import BaseClass
from datetime import datetime, timedelta


class TestFlight(BaseClass):
    today_date = datetime.today()
    departureDate = today_date.strftime("%d/%m/%Y")
    returnDate = (today_date + timedelta(2)).strftime("%d/%m/%Y")

    def test_shortFlight(self):
        base_page = BasePage(self.driver)
        flight_page = base_page.goToFlights()

        self.selectOptionByText(flight_page.getOrigin(), "Merida")
        self.selectOptionByText(flight_page.getDestination(), "La Habana")

        flight_page.getDepartingDate().send_keys(self.departureDate)
        flight_page.getReturninDate().send_keys(self.returnDate)
        flight_page.search()

        result_page = ResultPage(self.driver)
        self.selectOptionByText(result_page.getSortPrices(), "desc")
