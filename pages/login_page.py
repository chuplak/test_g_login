"""
Module for Login page functionality
"""
from pypom import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    """
    Class holds Login page functionality
    """

    _email_or_phohe_field = (By.ID, "identifierId")
    _next = (By.XPATH, "//span[contains(@class, 'VfPpkd-vQzf8d')]")


    def __init__(self, driver):
        """
        :param driver: WebDriver instance
        """
        super().__init__(driver)
        self.wait_for_page_to_load()

    @property
    def loaded(self):
        return self.wait.until(lambda x: self.is_element_present(*self._email_or_phohe_field))

