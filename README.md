## 🐯 Автотесты Python + Selenium + Allure

<img src="https://camo.githubusercontent.com/0803dd070e693cce45f8ba4b9821fbd9cd3aad1b41345ace8d507785532fb818/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d616465253230776974682d507974686f6e2d3166343235662e737667" 
alt="made-with-python" data-canonical-src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" style="max-width: 100%;"> 
<img src="https://camo.githubusercontent.com/0d572227ae7c34ecd4f55e28ec9e51c5ed9dea8ab5edbf0bf2116887d5d208dc/68747470733a2f2f62616467656e2e6e65742f62616467652f69636f6e2f76697375616c73747564696f3f69636f6e3d76697375616c73747564696f266c6162656c" 
alt="Visual Studio" data-canonical-src="https://badgen.net/badge/icon/visualstudio?icon=visualstudio&amp;label" style="max-width: 100%;">
> Тестирование фронта

### ✔ Онлайн-гипермаркет 21vek.by
Сайт: https://www.21vek.by/

Проект: [папка проекта](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/tree/main/selenium2.0/test), [файл с тестами](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/selenium2.0/test/test_main.py), [отчёт allure](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/tree/main/selenium2.0/results)

Allure:

<img src="https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/Allure/Screenshot_1.png"  width="450" style="max-width: 100%;"> <img src="https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/Allure/Screenshot_2.png"  width="850" style="max-width: 100%;">

1. [Проверка на позитивный кейс авторизации:](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/selenium2.0/test/test_main.py)

* Открыть сайт
* Принять cookie
* Нажать "Аккаунт"
* Нажать "Войти"
* Ввести правильный логин
* Ввести правильный пароль
* Нажать "Войти"
* Нажать "Аккаунт"
* Нажать "Выход"

2. [Проверка логики восстановления пароля:](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/selenium2.0/test/test_main.py)

* Открыть сайт
* Нажать "Аккаунт"
* Нажать "Войти"
* Ввести правильный логин
* Нажать «Забыли пароль»
* Ввести свой емейл
* Проверить, что получили нужный текст

3. [Проверка на негативный кейс авторизации:](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/selenium2.0/test/test_main.py)

* Открыть сайт
* Нажать "Аккаунт"
* Нажать "Войти"   
* Ввести правильный логин
* Ввести НЕправильный пароль
* Нажать войти
* Проверить, что получили нужный текст

4. [Проверка на негативный кейс авторизации:](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/selenium2.0/test/test_main.py)

* Открыть сайт
* Нажать "Аккаунт"
* Нажать "Войти"
* Ввести НЕправильный логин
* Ввести правильный пароль
* Нажать войти
* Проверить, что получили нужный текст

5. [Проверка на негативный кейс валидации:](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/selenium2.0/test/test_main.py)

* Открыть сайт
* Нажать "Аккаунт"
* Нажать "Войти"  
* Ввести логин без @
* Ввести правильный пароль
* Нажать войти
* Проверить, что получили нужный текст

6. [Проверка покупки товаров на сайте:](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/selenium2.0/test/test_main.py)

* Открыть сайт
* Нажать "Аккаунт"
* Нажать "Войти"
* Ввести правильный логин
* Ввести правильный пароль
* Нажать "Войти"
* Ввести "Ноутбук HP" в строку поиска
* Проскролить до нужного элемента
* Открыть страницу товара
* Отправить товар в корзину
* Нажать на вкладку "Корзина"
* Проверить,что товар в корзине(появилась кнопка "Оформить заказ")
* Удалить товар с корзины 
