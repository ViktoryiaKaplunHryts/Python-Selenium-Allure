## 🐯 Автотесты Python + Selenium + Allure

<img src="https://camo.githubusercontent.com/0803dd070e693cce45f8ba4b9821fbd9cd3aad1b41345ace8d507785532fb818/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d616465253230776974682d507974686f6e2d3166343235662e737667" 
alt="made-with-python" data-canonical-src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" style="max-width: 100%;"> 
<img src="https://camo.githubusercontent.com/0d572227ae7c34ecd4f55e28ec9e51c5ed9dea8ab5edbf0bf2116887d5d208dc/68747470733a2f2f62616467656e2e6e65742f62616467652f69636f6e2f76697375616c73747564696f3f69636f6e3d76697375616c73747564696f266c6162656c" 
alt="Visual Studio" data-canonical-src="https://badgen.net/badge/icon/visualstudio?icon=visualstudio&amp;label" style="max-width: 100%;">

### ✔ Как установить Selenium WebDriver:

__1.__ Скачиваем Chrome: <https://www.google.com.sg/intl/en/chrome/>
  
__2.__ Скачиваем гугл драйвер:

  * __Переходим по ссылке__ <https://sites.google.com/chromium.org/driver/>

  * __Далее:__

   ![](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0/Screenshot_1.png)

  * __Далее:__

   ![](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0/Screenshot_2.png)

   * __Выбираем__ ```chromedriver``` под вашу ОС и скачиваем

   ![](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0/Screenshot_3.png)

__3.__ На диске C создаем папку ```chromedriver```

__4.__ В папку ```chromedriver``` извлекаем ранее скаченные материалы

__5.__ Добавляем созданную папку в ```path```:
  
   __Цепочка действий:__ ```Параметры системы - О системе - Дополнительные параметры системы - Переменные среды - Системные переменные - Находим раздел path - 2 раза кликаем по нему - Создать - И добавляем путь C:\chromedriver- ОК```
    
__6.__ Проверяем работу через командную строку в Windows:

__Цепочка действий:__ ```Наводим указатель курсора на значок меню «Пуск» — Кликаем правой кнопкой мыши  — В появившемся контекстном меню выбераем пункт «Командная строка (администратор)», кликнув по нему левой кнопкой мышки - Подтверждаем свои намерения в окне контроля учетных записей, нажав «Да» - Пишем path - Должны найти наш установленный chromedriver```

У path есть особенность, что можно получить доступ к элементу, поэтому далее прописываем в командной строке название папки chromedriver, нажимаем Enter. Должно прийти сообщение 👇

![](https://github.com/ViktoryiaKaplunHryts/Python-Selenium-Allure/blob/main/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0/Screenshot_4.png)

### ✔ Как запустить виртуальное окружение в Python:

```Windows```

__1.__ Создадим на рабочем столе папку Selenium и откроем её с помощью VS Code от имени администратора

__2.__ Перейдем в каталог проекта в PowerShell, выполним код ниже, появится папка env, содержащая файлы виртуального окружения
  
```python -m venv env```

__3.__ Изменим политику, в PowerShell, пропишем

```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```

__4.__ Войдем в папку окружения (env), выполнив команду

```env\Scripts\activate.ps1```

__5.__ Установим Selenium

```pip install selenium```

__6.__ Далее можем прописать ```pip list``` и проверить, что Selenium установился

__7.__ В папке Selenium создаем папку first_lesson  и в ней создаем файл first.py, в котором прописываем и запускаем свой код

### ✔ Как поставить  и запустить Allure на Windows:

__1.__ Сначала ставим Scoop (делается 1 раз). Scoop - это приложение, которое необходимо для того, чтобы ставить программы, через командную строку:

* Открываем командную строку с правами администратора и прописываем команду

  ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```

И соглашаемся на изменения, прописывая Y

* Далее прописываем команду

  ```iex "& {$(irm get.scoop.sh)} -RunAsAdmin"```

* В качестве проверки прописываем команду

  ```scoop help```

__2.__ Ставим Allure, используя Scoop:

* В командной строке прописываем следующую команду:

  ```scoop install allure```

> Поскольку allure – java-приложение, на компьютере должна быть установлена JAVA

__3.__ Ставим Java, используя Scoop:

* В командной строке прописываем следующую команду:

  ```scoop bucket add java``` нажимаем Enter, далее прописываем

  ```scoop install openjdk```

 __4.__ Запускаем Allure:

 * В командной строке прописываем следующую команду:

   ``` cd i:\github\allure-2.9.0\bin\``` ( переходим в каталог с Allure ), далее

   ``` .\allure.bat```

__5.__ Генерируем каталог для хранения результатов прагона тестов:

* В папке проекта, создаем папку ```my_allure_results```  и дабавляем в папку ```.gitignore```

__6.__ Настраиваем аргументы для того, чтобы Allure знал, умел и понимал, что результаты прогонов нужно складывать в определенный каталог:

*  В папке проекта открываем папку ```vscode```  и в  файле ```settings.json```,  прописываем код

  ```
{
    "python.testing.pytestArgs": [
        "test",
"--alluredir-my_allure_results",
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```
Теперь после каждого прогона будет заполняться папка ```my_allure_results``` результатами прогонов

__7.__ Запускаем дашборд:

* В командной строке прописываем следующую команду:

  ``` .\allure.serve  "путь к папке где находятся результаты прогонов" ```

### ✔ Ну и наконец мои автотесты 😊

> Тестирование фронта

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
