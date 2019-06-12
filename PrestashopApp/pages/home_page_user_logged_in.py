from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from pages.login_page import LoginPage
from pages.page_base import PageBase


class HomePageUserLoggedIn(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
