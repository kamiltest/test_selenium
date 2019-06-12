import pytest
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from pages.home_page_user_logged_in import HomePageUserLoggedIn

EMAIL = "tester@wsb.wroclaw.pl"
PASSWORD = "tester123"


def test_home_page(prestashop_app):
    assert "PrestaShop Demo" in prestashop_app.get_title()


def test_user_login(prestashop_app):
    login_page = prestashop_app.go_to_login_page()
    home_page_logged_in = login_page.log_in_using_credentials(EMAIL, PASSWORD)
    assert home_page_logged_in is not None


def test_user_logout(prestashop_app):
    home_page_logged_in = HomePageUserLoggedIn(prestashop_app.driver)
    home_page = home_page_logged_in.sign_out()
    assert home_page is not None
