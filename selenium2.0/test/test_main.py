# Импортируем модули и отдельные классы
"""
2024 (c) Интернет -магазин "21 век.by"
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


# Создаем переменную с тестируемым сайтом
URL = 'https://www.21vek.by/'


# Positive test: запускаем тест с текстурой browser
def test_positive(browser):
    """
    SMK-1. Positive test
    """
    # Переходим на адрес тестируемой страницы
    browser.get(URL)
    
    # Ищем кнопку "Принять"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='AgreementCookie'] button[class*='blue-primary']")
    
    time.sleep(2)
    
    # Проверяем текст на кнопке
    assert button.text == 'Принять', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Аккаунт"
    button = browser.find_element(By.CSS_SELECTOR, value='span.userToolsText')
    # Проверяем текст на кнопке
    assert button.text == 'Аккаунт', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='userTools'] div[class*='buttonText']")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Вводим правильный email
    email = browser.find_element(By.CSS_SELECTOR, value="#login-email")    
    email.click()
    email.send_keys("gric.vika@mail.ru")

    # Вводим правильный пароль
    password = browser.find_element(By.CSS_SELECTOR, value="#login-password")
    password.click()
    password.send_keys("gv8061986")

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="button[class*='VyAyj'] div")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    time.sleep(2)
    
    # Ищем кнопку "Аккаунт"
    button = browser.find_element(By.CSS_SELECTOR, value='span.userToolsText')
    # Проверяем текст на кнопке
    assert button.text == 'Аккаунт', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Выход"
    button = browser.find_element(By.CSS_SELECTOR, value='div[class*="profile-logout-button"]')
    # Проверяем текст на кнопке
    assert button.text == 'Выход', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    
    # Password Recovery Test: запускаем тест с текстурой browser
def test_password_recovery(browser):
    """
    SMK-2. Password Recovery Test
    """
    # Переходим на адрес тестируемой страницы
    browser.get(URL)

    # Ищем кнопку "Аккаунт"
    button = browser.find_element(By.CSS_SELECTOR, value='span.userToolsText')
    # Проверяем текст на кнопке
    assert button.text == 'Аккаунт', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='userTools'] div[class*='buttonText']")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Вводим правильный email
    email = browser.find_element(By.CSS_SELECTOR, value="#login-email")    
    email.click()
    email.send_keys("gric.vika@mail.ru")

    # Ищем кнопку "Забыли пароль"
    button = browser.find_element(By.CSS_SELECTOR, value="button[class*='resetPasswordLink'] div")
    # Проверяем текст на вкладке
    assert button.text == 'Забыли пароль', "Unexpected text on button"    
    button.click()

    # Вводим правильный email
    email = browser.find_element(By.CSS_SELECTOR, value="#reset-password-email")    
    email.click()
    email.send_keys("gric.vika@mail.ru")

    # Ищем кнопку "Отправить"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='submitContainer'] button")
    # Проверяем текст на кнопке
    assert button.text == 'Отправить', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()
    
    time.sleep(2)

    # Выбираем модальное окно
    modal = browser.find_element(By.CSS_SELECTOR, value="div[class*='SuccessScreen'] h5")
    # Проверяем, что в модальном окне появилась нужная надпись
    assert modal.text == "Письмо отправлено", "Unexpected text on modal" 
    
    
    # Negative authorization case(Incorrect password): запускаем тест с текстурой browser
def test_incorrect_password(browser):
    """
    SMK-3. Entering an incorrect password
    """
    # Переходим на адрес тестируемой страницы
    browser.get(URL)

    # Ищем кнопку "Аккаунт"
    button = browser.find_element(By.CSS_SELECTOR, value='span.userToolsText')
    # Проверяем текст на кнопке
    assert button.text == 'Аккаунт', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='userTools'] div[class*='buttonText']")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Вводим правильный email
    email = browser.find_element(By.CSS_SELECTOR, value="#login-email")    
    email.click()
    email.send_keys("gric.vika@mail.ru")

    # Вводим НЕправильный пароль
    password = browser.find_element(By.CSS_SELECTOR, value="#login-password")
    password.click()
    password.send_keys("gv8061987")

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="button[class*='VyAyj'] div")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()
    
    time.sleep(2)

    # Проверка нужного текста
    password_label = browser.find_element(By.CSS_SELECTOR, value="span.styles_errorText__LEN7M")
    # Проверяем текст
    assert password_label.text == 'Неправильный пароль. \nСбросить пароль?', "Unexpected text on password_label"


    # Negative authorization case(Incorrect login): запускаем тест с текстурой browser
def test_incorrect_login(browser):
    """
    SMK-4. Entering an incorrect login
    """
    # Переходим на адрес тестируемой страницы
    browser.get(URL)

    time.sleep(2)

    # Ищем кнопку "Аккаунт"
    button = browser.find_element(By.CSS_SELECTOR, value='span.userToolsText')
    # Проверяем текст на кнопке
    assert button.text == 'Аккаунт', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='userTools'] div[class*='buttonText']")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Вводим НЕправильный email
    email = browser.find_element(By.CSS_SELECTOR, value="#login-email")    
    email.click()
    email.send_keys("griz.vika@mail.ru")

    # Вводим правильный пароль
    password = browser.find_element(By.CSS_SELECTOR, value="#login-password")
    password.click()
    password.send_keys("gv8061986")

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="button[class*='VyAyj'] div")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    time.sleep(2)

    # Проверка нужного текста
    email_label = browser.find_element(By.CSS_SELECTOR, value="span.styles_errorText__LEN7M")
    # Проверяем текст
    assert email_label.text == 'Проверьте электронную почту или \nзарегистрируйтесь', "Unexpected text on email_label"


   # Validation check : запускаем тест с текстурой browser
def test_validation_check(browser):
    """
    SMK-5. Validation check
    """
    # Переходим на адрес тестируемой страницы
    browser.get(URL)

    time.sleep(2)

    # Ищем кнопку "Аккаунт"
    button = browser.find_element(By.CSS_SELECTOR, value='span.userToolsText')
    # Проверяем текст на кнопке
    assert button.text == 'Аккаунт', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='userTools'] div[class*='buttonText']")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Вводим email без @
    email = browser.find_element(By.CSS_SELECTOR, value="#login-email")    
    email.click()
    email.send_keys("griс.vikamail.ru")

    # Вводим правильный пароль
    password = browser.find_element(By.CSS_SELECTOR, value="#login-password")
    password.click()
    password.send_keys("gv8061986")

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="button[class*='VyAyj'] div")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Проверка нужного текста
    email_label = browser.find_element(By.CSS_SELECTOR, value="span[class*='module__message']")
    # Проверяем текст
    assert email_label.text == 'Неправильный формат электронной почты', "Unexpected text on email_label"
    
    
    # Purchase of goods : запускаем тест с текстурой browser
def test_purchase_of_goods(browser):
    """
    SMK-6. Purchase of goods
    """
    # Переходим на адрес тестируемой страницы
    browser.get(URL)

    time.sleep(5)

    # Ищем кнопку "Аккаунт"
    button = browser.find_element(By.CSS_SELECTOR, value='span.userToolsText')
    # Проверяем текст на кнопке
    assert button.text == 'Аккаунт', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='userTools'] div[class*='buttonText']")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Вводим правильный email
    email = browser.find_element(By.CSS_SELECTOR, value="#login-email")    
    email.click()
    email.send_keys("gric.vika@mail.ru")

    # Вводим правильный пароль
    password = browser.find_element(By.CSS_SELECTOR, value="#login-password")
    password.click()
    password.send_keys("gv8061986")

    # Ищем кнопку "Войти"
    button = browser.find_element(By.CSS_SELECTOR, value="button[class*='VyAyj'] div")
    # Проверяем текст на кнопке
    assert button.text == 'Войти', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    time.sleep(2)

    # Ищем поисковую строку
    search = browser.find_element(By.CSS_SELECTOR, value="#catalogSearch")

    # Находим атрибут нужного значения (перед вводом текста)
    search_text = search.get_attribute("value")
    assert search.text == "", "Unexpected attribute value"

    # Вводим текст в строку поиска
    search.send_keys("Ноутбук HP")

    # Нажимаем кнопку enter
    search.send_keys(Keys.ENTER)

    # Проверяем, что значение атрибута изменилось(после ввода текста)
    search = browser.find_element(By.CSS_SELECTOR, value="#catalogSearch")
    search_text = search.get_attribute("value")
    assert search_text == "Ноутбук HP", "Unexpected attribute value"

    time.sleep(5)

    # Скролим до нужного элемента
    element = browser.find_element(By.CSS_SELECTOR, value="span[class*='7770541']")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

    # Открываем вкладку нужного товара
    element = browser.find_element(By.CSS_SELECTOR, value="[data-code='8619455'] img")
    element.click()
    
    time.sleep(5)

    # Отправляем товар в корзину
    element = browser.find_element(By.CSS_SELECTOR, value="button[class*='RB62D']")
    element.click()
    
    time.sleep(2)

    # Открываем корзину
    element = browser.find_element(By.CSS_SELECTOR, value="span.headerCartLabel")
    element.click()

    # Проверяем,что товар в корзине(появилась кнопка "Оформить заказ")
    button = browser.find_element(By.CSS_SELECTOR, value="button[class*='OrderPrice']")
    assert button.text == 'Оформить заказ', "Unexpected text on button"

    # Ищем кнопку "Удалить"
    button = browser.find_element(By.CSS_SELECTOR, value=" div[class*='buttonsBlock__HkKKZ'] button:nth-child(1)")
    
    time.sleep(5)

    # Проверяем текст на кнопке
    assert button.text == 'Удалить', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    # Ищем кнопку "Удалить" в модальном окне
    button = browser.find_element(By.CSS_SELECTOR, value="div[class*='Wrapper__kdVt'] button[class*='pink-primary'] div")
    # Проверяем текст на кнопке
    assert button.text == 'Удалить', "Unexpected text on button"
    # Кликаем по кнопке
    button.click()

    
     

   
    
    

    
    


    
    
    
    
    
    

    
    
    
    

