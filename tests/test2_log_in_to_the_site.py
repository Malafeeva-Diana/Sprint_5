from locators import LocatorsPage
from data import *


class TestLogInToTheSite:

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_button_log_in_main_page(self, driver):
        driver.find_element(*LocatorsPage.button_log_in_account).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_enter_pass).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        enter_butt_test = driver.find_element(*LocatorsPage.button_log_in).text
        assert enter_butt_test == 'Войти'

    # Вход через кнопку «Личный кабинет»
    def test_button_log_personal_account(self, driver):
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_enter_pass).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        enter_butt_test = driver.find_element(*LocatorsPage.button_log_in).text
        assert enter_butt_test == 'Войти'

    # Вход через кнопку в форме регистрации
    def test_button_log_in_registration_form(self, driver):
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.registerate).click()
        driver.find_element(*LocatorsPage.butt_in_enter).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_enter_pass).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        enter_butt_test = driver.find_element(*LocatorsPage.button_log_in).text
        assert enter_butt_test == 'Войти'

    # Вход через кнопку в форме восстановления пароля
    def test_log_butt_in_pass_recovery(self, driver):
        driver.find_element(*LocatorsPage.account_butt).click()
        driver.find_element(*LocatorsPage.butt_log_in_pass).click()
        driver.find_element(*LocatorsPage.butt_in_enter).click()
        driver.find_element(*LocatorsPage.input_email).send_keys(email)
        driver.find_element(*LocatorsPage.input_enter_pass).send_keys(password)
        driver.find_element(*LocatorsPage.button_log_in).click()
        enter_butt_test = driver.find_element(*LocatorsPage.button_log_in).text
        assert enter_butt_test == 'Войти'
