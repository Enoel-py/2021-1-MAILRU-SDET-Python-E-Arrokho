import pytest
import time
from BasePage.Base import BaseCase
from ui.locators.locators import MainPageLocators


EMAIL = 'enoel98@mail.ru'
PASSWORD = 'AutoUseTesting'


def test_login(browser):
    main_page = BaseCase(browser)
    main_page.open_site()
    main_page.login(EMAIL, PASSWORD)
    main_page.driver.implicitly_wait(10)
    assert main_page.check_element(MainPageLocators.INSTRUCTION_MODULE)


def test_logout(browser):
    main_page = BaseCase(browser)
    main_page.open_site()
    main_page.login(EMAIL, PASSWORD)
    time.sleep(1)
    main_page.logout()
    assert main_page.check_element(MainPageLocators.MAIN_PAGE_TITLE)


def test_edit_contacts(browser):
    new_contacts = 'Anton'
    main_page = BaseCase(browser)
    main_page.open_site()
    main_page.login(EMAIL, PASSWORD)
    main_page.driver.get('https://target.my.com/profile/contacts')
    main_page.type_word(MainPageLocators.CONTACTS_NAME, new_contacts)
    main_page.click(MainPageLocators.CONTACTS_SAVE)
    assert main_page.check_element(MainPageLocators.CONTACTS_SAVE_SUCCES)


@pytest.mark.parametrize(
    "locator_menu, locator_check",
    [
        pytest.param(MainPageLocators.CM_BILLING, MainPageLocators.BILLING_MENU),
        pytest.param(MainPageLocators.CM_STATISTICS, MainPageLocators.STATISTICS_MENU_STAT)
    ]
                         )
def test_menu(browser, locator_menu, locator_check):
    main_page = BaseCase(browser)
    main_page.open_site()
    main_page.login(EMAIL, PASSWORD)
    time.sleep(1)
    main_page.click(locator_menu)
    main_page.check_element(locator_check)
