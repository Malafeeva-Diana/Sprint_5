from data import *
from locators import LocatorsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import *


class TestRegistration:

    # Проверка успешной регистрации
    def test_successful_registration(self, driver):
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.registerate).click()
        driver.find_element(*LocatorsPage.name).send_keys(name)
        driver.find_element(*LocatorsPage.input_email).send_keys(generate_email())
        driver.find_element(*LocatorsPage.input_password).send_keys(generate_password())
        driver.find_element(*LocatorsPage.button_register).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsPage.button_log_in))
        enter_button_test = driver.find_element(*LocatorsPage.button_log_in).text
        assert enter_button_test == 'Войти'

    # Проверка для некорректного пароля
    def test_check_incorrect_password(self, driver):
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.registerate).click()
        driver.find_element(*LocatorsPage.name).send_keys(name)
        driver.find_element(*LocatorsPage.input_email).send_keys(generate_email())
        driver.find_element(*LocatorsPage.input_password).send_keys(incorrect_password)
        driver.find_element(*LocatorsPage.button_register).click()
        incorrect_pass = driver.find_element(*LocatorsPage.error_field_password).text
        assert incorrect_pass == 'Некорректный пароль'
