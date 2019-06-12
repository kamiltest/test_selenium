from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.page_base import PageBase
from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="_desktop_user_info"]/div/a/span')))
            return True
        except Exception as e:
            print(e)
            return False

    def go_to_login_page(self):
        self.button_sign_in.click()
        login_page = LoginPage(self.driver)
        return login_page if login_page.is_open() else None
