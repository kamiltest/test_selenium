import pytest
from selenium import webdriver


@pytest.fixture()
def chromedriver(request):
    driver = webdriver.Chrome(executable_path="webdriver\\chromedriver.exe")

    def chromedriver_teardown():
        driver.close()

    request.addfinalizer(chromedriver_teardown)
    return driver


@pytest.fixture()
def prestashop_driver(chromedriver):
    chromedriver.get("http://demo.prestashop.com/")
    return chromedriver


def test_main_page(prestashop_driver):
    assert "PrestaShop Demo" in prestashop_driver.title
