from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.page_base import PageBase


class HomePageUserLoggedIn(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def is_open(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="_desktop_user_info"]/div/a[1]/i')))
            return True
        except Exception as e:
            print(e)
            return False