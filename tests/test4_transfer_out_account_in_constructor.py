from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import *
from locators import LocatorsPage


class TestTransferOutAccount:
    # Проверка перехода из личного кабинета в конструктор по клику на «Конструктоо».
    def test_check_transfer_to_constructor_from_account_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsPage.account_butt))
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_password).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsPage.construction_butt))
        driver.find_element(*LocatorsPage.construction_butt).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверка перехода из личного кабинета в конструктор по клику на логотип сайта
    def test_check_tap_logo_transfer_to_constructor_from_account_page(self, driver):
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_password).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        driver.find_element(*LocatorsPage.account_butt).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsPage.logo_page))
        driver.find_element(*LocatorsPage.logo_page).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
