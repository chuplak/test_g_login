"""Base page functionality"""

from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(Page):
    """
    Class holds BasePage functionality
    """

    _page_title = (By.XPATH, '/html/head/title')
    _h1 = (By.XPATH, '//input[contains(@name, "q")]')
    _sign_in_1 = (By.XPATH, '//a[contains(text(), "Sign in")]')

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """
        :param driver: WebDriver instance
        :param timeout: Time to wait for specified expected condition
        """
        super().__init__(driver, timeout=timeout)

    @property
    def loaded(self):
        return self.wait.until(lambda x: self.is_element_present(*self._h1))

    @property
    def page_title(self):
        return self.find_element(*self._page_title)

    @property
    def sign_in(self):
        return self.find_element(*self._sign_in_1)

    def press_sign_in(self):
        """

        :return:
        """
        self.sign_in.click()
