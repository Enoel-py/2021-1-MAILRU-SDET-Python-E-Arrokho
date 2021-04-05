import pytest
import time
from BasePage.Base import BaseCase
from ui.locators.locators import BasePageLocators
from ui.pages import base_page

EMAIL = 'enoel98@mail.ru'
PASSWORD = 'AutoUseTesting'


class Test(BaseCase):
    def test_login_negative1(self):
        self.base_page.login('er'+EMAIL,PASSWORD)
        time.sleep(2)
        assert self.driver.current_url != self.base_page.url

    def test_login_negative2(self):
        self.base_page.login(EMAIL,PASSWORD+'1')
        time.sleep(2)
        assert self.driver.current_url != self.base_page.url