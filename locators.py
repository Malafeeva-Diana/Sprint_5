from selenium.webdriver.common.by import By


class LocatorsPage:

    """ Кнопка Личный кабинет"""
    account_butt = (By.XPATH, "//a[@href = '/account']")

    """Кнопка зарегать"""
    registerate = (By.XPATH, "//a[@href = '/register']")

    """Кнопка «Зарегистрироваться» на странице регистрации"""
    button_register = (By.XPATH, "//button[text()='Зарегистрироваться']")

    """Поле имя"""
    name = (By.XPATH, './/input[@name="name"]')

    """Email на странице Входа и на странице регистрации"""
    input_email = (By.XPATH, ".//*[text()='Email']/following-sibling::input")

    """Пароль на странице Входа и на странице регистрации"""
    input_password = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")

    """Текст вход на странице"""
    log_in_text = (By.XPATH, ".// h2[text() = 'Вход']")

    """Кнопка «Войти в аккаунт» на главной странице"""
    button_log_in_account = (By.XPATH, './/button[contains(text(),"Войти в аккаунт")]')

    """Кнопка «Выход» в личном кабинете"""  #
    button_exit = (By.XPATH, "//button[contains(text(),'Выход')]")

    """«Некорректный пароль» на странице Входа"""
    error_field_password = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    """Кнопка конструктора"""
    construction_butt = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    """Инпут пароль на странице Входа"""
    input_enter_pass = (By.XPATH, './/input[@name="Пароль"]')

    """Кнопка «Войти» на странице Входа"""
    button_log_in = (By.XPATH, "//button[text()='Войти']")

    """Кнопка восстановить пароль на странице регистрации  и восстановления пароля"""
    butt_log_in_pass = (By.XPATH, ".//a[text()='Восстановить пароль']")

    """Кнопка войти на странице восстановления пароля"""
    butt_in_enter = (By.XPATH, "//a[@href = '/login']")

    """Логотип сайт стелла бургер"""
    logo_page = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

    """Кнопка раздела «Начинки» в Конструкторе"""
    filling_constructor = (By.XPATH, "//span[text()='Начинки']")

    """Кнопка раздела «Соусы» в Конструкторе"""
    sauce_constructor = (By.XPATH, "//span[text()='Соусы']")

    """Кнопка раздела «Булки» в Конструкторе"""
    bread_constructor = (By.XPATH, "//span[text()='Булки']")

    """Текст раздела «Соусы» в Конструкторе"""
    header_sauce_constructor = (By.XPATH, "//h2[text()='Соусы']")

    """Текст раздела «Начинки» в Конструкторе"""
    header_filling_constructor = (By.XPATH, "//h2[text()='Начинки']")

    """Текст раздел  «Булки» в Конструкторе"""
    header_bread_constructor = (By.XPATH, "//h2[text()='Булки']")

    """Выбранный таб в конструкторе"""
    select_tab_constructor = (By.XPATH, ".//div[contains(@class, 'current')]/span")