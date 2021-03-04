import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyElementClickable(self, id):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, id))
        )

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def selectOptionByValue(self, locator, value):
        sel = Select(locator)
        sel.select_by_value(value)
