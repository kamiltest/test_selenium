from selenium.webdriver.remote.webdriver import WebDriver


class PageBase(object):

    IMPLICITY_WAIT = 10

    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(self.IMPLICITY_WAIT)

    @property
    def driver(self):
        """
        :rtype: WebDriver
        """
        return self._driver

    def get_title(self):
        return self._driver.title

    @property
    def header_logo(self):
        """
        :rtype: WebElement
        """
        return self.driver.find_element_by_css_selector('.logo')

    @property
    def button_sign_in(self):
        return self.driver.find_element_by_xpath('//*[@id="_desktop_user_info"]/div/a/span')

    @property
    def button_sign_out(self):
        return self.driver.find_element_by_xpath('//*[@id="_desktop_user_info"]/div/a[1]/i')
