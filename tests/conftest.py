import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\selenium\\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\\selenium\\msedgedriver.exe")

    driver.get("file:///C:/automation/site/index.html")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
