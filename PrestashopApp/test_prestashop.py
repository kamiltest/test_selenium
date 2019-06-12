import pytest
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from pages.home_page import HomePage


EMAIL = "tester@wsb.wroclaw.pl"
PASSWORD = "tester123"


def test_home_page(prestashop_app):
    assert "PrestaShop Demo" in prestashop_app.get_title()


def test_user_login(prestashop_app):
    login_page = prestashop_app.go_to_login_page()
    login_page.input_email.send_keys(EMAIL)
    login_page.input_password.send_keys(PASSWORD)
    login_page.button_submit.click()

    # TODO:
    # home_page_logged_in = login_page.log_in_using_credentials(EMAIL, PASSWORD)
    # assert home_page_logged_in.is_open()

    time.sleep(10)
