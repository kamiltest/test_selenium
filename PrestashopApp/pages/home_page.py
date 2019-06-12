from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.login_page import LoginPage
from pages.page_base import PageBase


class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.button_sign_in.click()
        login_page = LoginPage(self.driver)
        return login_page if login_page.is_open() else None
