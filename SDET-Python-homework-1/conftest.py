import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    driver_path = 'C:/Users/Антон/Google Диск/Pytest/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    yield driver
    driver.quit()
