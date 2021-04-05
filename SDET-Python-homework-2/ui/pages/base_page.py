import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from ui.locators.locators import BasePageLocators
from utils.decorators import wait

WAIT_TIME = 5
CLICK_RETRY = 3
BASE_TIMEOUT = 5

class PageNotLoadedException(Exception):
    pass


class BasePage:
    url = 'https://target.my.com/'
    locators = BasePageLocators()

    def __init__(self, driver):
        self.page_source = None
        self.driver = driver
        self.main_page_url = "https://target.my.com/"
        assert self.is_opened()

    # Открыть сайт
    def open_site(self):
        return self.driver.get(self.main_page_url)

    # Найти элемент на странице по локатору
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))



    # Клик по элементу
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    # Проверка существования элемента на странице
    def check_element(self, locator):
        try:
            self.find(locator)
        except NoSuchElementException:
            return False
        return True

    # Напечатать текст в поле для ввода по локатору
    def type_word(self, locator, word):
        input_form = self.find(locator)
        input_form.clear()
        input_form.send_keys(word)

    # Авторизация на сайте
    def login(self, email, password):
        self.click(BasePageLocators.MAIN_LOGIN_LOCATOR)
        email_input = self.find(BasePageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.find(BasePageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        self.find(BasePageLocators.LOGIN).click()
        time.sleep(1)

    # Выход из личного кабинета
    def logout(self):
        self.click(BasePageLocators.RIGHT_MENU)
        WebDriverWait(self.driver, WAIT_TIME). \
            until(EC.presence_of_element_located(BasePageLocators.MENU))
        time.sleep(1)
        self.click(BasePageLocators.LOGOUT)

    def is_opened(self):
        def _check_url():
            if self.driver.current_url != self.url:
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {BASE_TIMEOUT} for {self.__class__.__name__}.\n'
                    f'Current url: {self.driver.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=BASE_TIMEOUT, interval=0.1)

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
