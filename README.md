# Финальный проект 5 спринта автоматизации

## UI-тестирование

Для тестирования был выбран сервис [Stella Burgers](https://stellarburgers.nomoreparties.site/).


 <details> <summary> Файлы </summary>

> tests - директория с тестами
> 
>
>conftest.py - фикстуры
> 
>data.py - набор тд 
>
> locators.py - локаторы 
> 
>helpers.py - генераторы логина и пароля

</details>


<details> <summary> Регистрация </summary>

Успешная регистрация
- Поле «Имя» должно быть не пустым
- Поле Email введён email в формате логин@домен
- Пароль — минимум шесть символов

Ошибка для некорректного пароля
</details>


<details> <summary> Вход </summary>

- Вход по кнопке «Войти в аккаунт» на главной
- Вход через кнопку «Личный кабинет»
- Вход через кнопку в форме регистрации
- Вход через кнопку в форме восстановления пароля
</details>

<details> <summary> Переход в личный кабинет </summary>

- Переход по клику на «Личный кабинет»
</details>

<details> <summary>  Переход из личного кабинета в конструктор </summary>

- Переход по клику на «Конструктор» и на логотип Stellar Burgers
</details>

<details> <summary> Выход из аккаунта </summary>

- Выход по кнопке «Выйти» в личном кабинете
</details>

<details> <summary> Раздел «Конструктор» </summary>

- Переход к разделу «Соусы»
- Переход к разделу «Начинки»
- Переход к разделу «Булки»
</details>


>Для запуска тестов должны быть установлены:
pytest selenium