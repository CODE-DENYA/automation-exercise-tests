# 🎭 Automation Exercise — UI Test Automation Framework

Проект по автоматизации UI-тестирования веб-приложения [Automation Exercise](https://automationexercise.com/) с использованием **Python**, **Playwright** и **Pytest**.

[![UI Automated Tests](https://github.com/CODE-DENYA/automation-exercise-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/CODE-DENYA/automation-exercise-tests/actions/workflows/tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://CODE-DENYA.github.io/automation-exercise-tests/)

---

## 🛠 Технологический стек

* **Язык программирования:** Python 3.12
* **Фреймворк автоматизации:** Playwright (Sync API)
* **Тестовый раннер:** Pytest
* **Паттерн проектирования:** Page Object Model (POM)
* **Отчетность:** Allure Framework + Playwright Tracing (скриншоты и трассировка при падениях)
* **Генерация данных:** Faker + UUID (уникализация сущностей)
* **Качество кода:** Ruff (линтер)
* **Параллельный запуск:** pytest-xdist (`pytest -n 2`)
* **CI/CD:** GitHub Actions (автоматический запуск, линтинг и публикация Allure-отчета на GitHub Pages)

---

## 🧪 Покрытие тестами

Тестовый набор охватывает ключевые пользовательские сценарии E2E и критическую функциональность веб-приложения:

### 🔑 Авторизация и регистрация (`tests/test_auth.py`, `tests/test_delete_account.py`)
* **Проверка навигации:** Успешное открытие страницы входа и регистрации.
* **Негативный вход:** Валидация ошибки при авторизации с невалидными учётными данными (`Your email or password is incorrect!`).
* **Регистрация пользователя:** Полный цикл создания нового пользователя с генерацией динамических данных.
* **Проверка дубликата email:** Негативный сценарий регистрации на уже существующий email с предварительной очисткой сессии и кук (`Email Address already exist!`).
* **Удаление аккаунта:** Создание пользователя и его последующее удаление с валидацией сообщения `ACCOUNT DELETED!`.

### 🛍️ Каталог и карточки товаров (`tests/test_products.py`, `tests/test_product_details.py`)
* **Отображение каталога:** Проверка открытия витрины и видимости товаров.
* **Поиск товаров (DDT):** Параметризованный поиск по ключевым словам (`dress`, `tshirt`, `jean`) с использованием `@pytest.mark.parametrize`.
* **Карточка товара:** Валидация корректности отображения наименования, категории, цены и статуса наличия (`Availability`).

### 🛒 Корзина и оформление заказа (`tests/test_cart.py`, `tests/test_checkout.py`)
* **Работа с корзиной:** Добавление товара из каталога и его удаление с валидацией через built-in ожидания Playwright.
* **E2E Покупка товара:** Сквозной сценарий — регистрация нового аккаунта → сохранение сессии → добавление товара в корзину → оформление заказа и ввод платежных реквизитов карты → проверка подтверждения `ORDER PLACED!`.

### 📨 Обратная связь и сервисные функции (`tests/test_contact.py`, `tests/test_subscription.py`)
* **Contact Us:** Заполнение формы обратной связи с прикреплением файла (`tmp_path`) и обработкой native JS-диалога `alert`.
* **Подписка на рассылку:** Проверка отправки email на рассылку новостей в футере сайта.

---

## 🏗 Архитектурные особенности фреймворка

* **Page Object Model (POM):** Каждая страница приложения вынесена в отдельный класс в директории `pages/`, что исключает дублирование селекторов.
* **Устойчивые селекторы:** Использование атрибутов `data-qa` для надежного поиска элементов независимо от изменений верстки.
* **Блокировка рекламы (`conftest.py`):** Перехват запросов к рекламным сетям (Google Syndication, DoubleClick) через `page.route()` для устранения замедлений и флакующих падений.
* **Обход антибот-систем:** Маскировка браузерного контекста (настройка User-Agent и отключение `AutomationControlled`).
* **Автоматический сбор артефактов:** При упавшем тесте в Allure-отчет автоматически прикрепляется full-page скриншот и `.zip` архив Playwright Trace с детальными шагами.
* **Уникальность тестовых данных:** Генератор данных соединяет `Faker` и `uuid4`, исключая коллизии при параллельном запуске.

---

## 📁 Структура проекта

```text
automation-exercise-tests/
├── .github/
│   └── workflows/
│       └── tests.yml            # CI/CD пайплайн GitHub Actions
├── pages/                       # Page Object классы
│   ├── base_page.py             # Базовый класс для всех страниц
│   ├── cart_page.py             # Корзина товаров
│   ├── checkout_page.py         # Оформление заказа
│   ├── contact_page.py          # Форма обратной связи
│   ├── delete_account_page.py   # Подтверждение удаления аккаунта
│   ├── login_page.py            # Авторизация и первичная регистрация
│   ├── product_details_page.py  # Карточка конкретного товара
│   ├── products_page.py         # Каталог товаров и поиск
│   └── signup_page.py           # Форма заполнения данных аккаунта
├── tests/                       # Автотесты (Pytest)
│   ├── test_auth.py             # Авторизация и регистрация
│   ├── test_cart.py             # Добавление и проверка товаров в корзине
│   ├── test_checkout.py         # E2E-сценарий оформления заказа
│   ├── test_contact.py          # Отправка формы обратной связи
│   ├── test_delete_account.py   # Сценарий удаления аккаунта
│   ├── test_product_details.py  # Проверка карточки товара
│   ├── test_products.py         # Поиск и фильтрация в каталоге
│   └── test_subscription.py     # Подписка на рассылку
├── utils/                       # Вспомогательные утилиты
│   └── data_generator.py        # Генератор фейковых данных (Faker + UUID)
├── .gitignore                   # Исключения Git
├── conftest.py                  # Pytest-фикстуры (браузер, трассировка, блокировка рекламы)
├── pytest.ini                   # Конфигурация Pytest и Allure
├── requirements.txt             # Зависимости проекта
└── README.md
```

---

## 🚀 Локальный запуск

### На Windows (PowerShell):
```bash
git clone https://github.com/CODE-DENYA/automation-exercise-tests.git
cd automation-exercise-tests

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
npx playwright install chromium
```

### На macOS / Linux / Git Bash:
```bash
git clone https://github.com/CODE-DENYA/automation-exercise-tests.git
cd automation-exercise-tests

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npx playwright install chromium
```

### Запуск тестов
* **Запуск всех тестов в 2 потока:**
  ```bash
  pytest -n 2
  ```
* **Запуск с генерацией Allure-результатов:**
  ```bash
  pytest --alluredir=allure-results
  ```
* **Просмотр Allure-отчета локально:**
  ```bash
  allure serve allure-results
  ```
* **Проверка стиля и качества кода (Ruff):**
  ```bash
  ruff check .
  ```

---

## 🔄 CI/CD Пайплайн

При каждом push или pull request в ветку `main` запускается GitHub Actions workflow:
1. Проводится статическая проверка кода с помощью **Ruff**.
2. Запускаются UI-тесты в 2 потока в headless-режиме.
3. Формируется и публикуется интерактивный отчет **Allure Report** на GitHub Pages.