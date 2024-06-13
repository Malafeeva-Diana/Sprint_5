from locators import LocatorsPage


class TestChangeSection:

    # Проверка, что работают переходы к разделу «Соусы»
    def test_open_sauce_section(self, driver):
        driver.find_element(*LocatorsPage.filling_constructor).click()
        driver.find_element(*LocatorsPage.sauce_constructor).click()
        assert driver.find_element(*LocatorsPage.select_tab_constructor).text == driver.find_element(
            *LocatorsPage.header_sauce_constructor).text

    # Проверка, что работают переходы к разделу «Начинки»
    def test_open_filling_section(self, driver):
        driver.find_element(*LocatorsPage.sauce_constructor).click()
        driver.find_element(*LocatorsPage.filling_constructor).click()
        assert driver.find_element(*LocatorsPage.select_tab_constructor).text == driver.find_element(
            *LocatorsPage.header_filling_constructor).text

    # Проверка, что работают переходы к разделу «Булки»
    def test_open_bread_section(self, driver):
        driver.find_element(*LocatorsPage.filling_constructor).click()
        driver.find_element(*LocatorsPage.bread_constructor).click()
        assert driver.find_element(*LocatorsPage.select_tab_constructor).text == driver.find_element(
            *LocatorsPage.header_bread_constructor).text
