from locators import LocatorsPage
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogOutInAccountPage:

    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_check_button_log_out_account_page(self, driver):
        driver.find_element(*LocatorsPage.button_log_in_account).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_password).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsPage.account_butt))
        driver.find_element(*LocatorsPage.account_butt).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsPage.button_exit))
        driver.find_element(*LocatorsPage.button_exit).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(LocatorsPage.log_in_text))
        log_out = driver.find_element(*LocatorsPage.log_in_text).text
        assert log_out == 'Вход'
