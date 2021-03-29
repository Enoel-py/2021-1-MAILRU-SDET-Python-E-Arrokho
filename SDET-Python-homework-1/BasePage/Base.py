from turtle import clear
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException

WAIT_TIME = 20


class BaseCase:

    def __init__(self, driver):
        self.page_source = None
        self.driver = driver
        self.main_page_url = "https://target.my.com/"

    # Открыть сайт
    def open_site(self):
        return self.driver.get(self.main_page_url)

    # Найти элемент на странице по локатору
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_element(self, locator, time=WAIT_TIME):
        return WebDriverWait(self.driver, time). \
            until(EC.presence_of_element_located(locator))

    # Клик по элементу
    def click(self, locator, time=WAIT_TIME):
        element = WebDriverWait(self.driver, time). \
            until(EC.element_to_be_clickable(locator))
        element.click()

    # Проверка существования элемента на странице
    def check_element(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    # Напечатать текст в поле для ввода по локатору
    def type_word(self, locator, word):
        input_form = self.find_element(locator)
        input_form.clear()
        input_form.send_keys(word)

    # Авторизация на сайте
    def login(self, email, password):
        self.find_element(MainPageLocators.MAIN_LOGIN_LOCATOR).click()
        email_input = self.find_element(MainPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.find_element(MainPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        self.find_element(MainPageLocators.LOGIN).click()
        time.sleep(1)

    # Выход из личного кабинета
    def logout(self):
        self.click(MainPageLocators.RIGHT_MENU)
        WebDriverWait(self.driver, WAIT_TIME). \
            until(EC.presence_of_element_located(MainPageLocators.MENU))
        time.sleep(1)
        self.click(MainPageLocators.LOGOUT)
