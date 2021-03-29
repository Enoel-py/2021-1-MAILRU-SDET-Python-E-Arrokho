from selenium.webdriver.common.by import By


class MainPageLocators:
    # Login
    MAIN_LOGIN_LOCATOR = (By.CSS_SELECTOR, 'div.responseHead-module-button-1BMAy4')  # Кнопка "ВОЙТИ"
    EMAIL_INPUT = (By.NAME, 'email')  # Поле для ввода email
    PASSWORD_INPUT = (By.NAME, 'password')  # Поле для ввода пароля
    LOGIN = (By.CSS_SELECTOR, 'div.authForm-module-button-2G6lZu')  # Войти в рекламный кабинет

    # Titles on Pages
    INSTRUCTION_MODULE = (By.CLASS_NAME, 'instruction-module-wrapper-1pOHw9')  # Заголовок с инструкциями после авторизации
    MAIN_PAGE_TITLE = (By.CLASS_NAME, 'mainPage-module-bigTitle-2-aiP9')  # Заголовок на главной станице до авторизации

    # LogOUT
    RIGHT_MENU = (By.CSS_SELECTOR, 'div.right-module-userNameWrap-34ibLS')  # Кнопка для открытия меню
    MENU = (By.CSS_SELECTOR, '.rightMenu-module-shownRightMenu-2p7e0v')  # Меню с "Пополнить.." и "Выйти"
    LOGOUT = (By.LINK_TEXT, 'ВЫЙТИ')  # Кнопка "Выйти"

    # Contacts
    CONTACTS = (By.CLASS_NAME, 'center-module-button-cQDNvq')
    CONTACTS_NAME = (By.CSS_SELECTOR, 'input.input__inp.js-form-element')  # Поле для ФИО
    CONTACTS_SAVE = (By.CLASS_NAME, 'button__text')  # Кнопка "Сохранить"
    CONTACTS_SAVE_SUCCES = (By.CSS_SELECTOR, 'div._notification__content.js-notification-content')  # "успешно изменено"

    # Center Menu
    CM_DASHBOARD = (By.CSS_SELECTOR, 'a.center-module-button-cQDNvq.center-module-campaigns-3hwOlL')
    CM_SEGMENTS = (By.CSS_SELECTOR, 'a.center-module-button-cQDNvq.center-module-segments-3y1hDo')
    CM_BILLING = (By.CSS_SELECTOR, 'a.center-module-button-cQDNvq.center-module-billing-x3wyL6')
    CM_STATISTICS = (By.CSS_SELECTOR, 'a.center-module-button-cQDNvq.center-module-statistics-26_XmT')
    CM_PRO = (By.CSS_SELECTOR, 'a.center-module-button-cQDNvq.center-module-pro-3rBU0K')

    # Segments
    #SEGMENTS_NAVIGATION = (By.CSS_SELECTOR, 'div.navigation-menu')
    STATISTICS_MENU_STAT = (By.XPATH, '//div[@cid="view107"]')  # Меню навигации по сегментам

    # Billing
    #BILLING_MENU = (By.CSS_SELECTOR, 'div.layout__page-tabs.js-layout-topBlock')
    BILLING_MENU = (By.XPATH, '//span[contains(text(), "Пополнение счёта")]')

    # Statistics
    STATISTICS_MENU_STAT = (By.XPATH, '//div[@cid="view128"]')  # Меню навигации по разделам статистики
