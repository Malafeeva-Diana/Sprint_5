from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import *
from locators import LocatorsPage


class TestTransferAccountPage:
    # Проверка перехода по клику на «Личный кабинет»
    def test_check_transfer_to_account_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsPage.account_butt))
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_password).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        driver.find_element(*LocatorsPage.account_butt).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
