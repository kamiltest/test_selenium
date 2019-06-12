import pytest
from selenium import webdriver

from pages.home_page import HomePage


@pytest.fixture(scope="session")
def chromedriver(request):
    driver = webdriver.Chrome(executable_path="webdriver\\chromedriver.exe")

    def chromedriver_teardown():
        driver.quit()

    request.addfinalizer(chromedriver_teardown)
    return driver


@pytest.fixture(scope="session")
def prestashop_app(chromedriver):
    """
    :type chromedriver: WebDriver
    :rtype: HomePage
    """
    prestashop = HomePage(chromedriver)
    prestashop.driver.get("http://demo.prestashop.com/")
    prestashop.driver.switch_to.frame(0)
    return prestashop
