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
* **Отчетность:** Allure Framework + Playwright Tracing
* **Генерация данных:** Faker
* **Качество кода:** Ruff (линтер)
* **Параллельный запуск:** pytest-xdist
* **CI/CD:** GitHub Actions (автоматический запуск тестов и публикация Allure-отчета на GitHub Pages)

---

## 📁 Структура проекта

```text
automation-exercise-tests/
├── .github/
│   └── workflows/
│       └── tests.yml            # CI/CD пайплайн GitHub Actions
├── pages/                       # Page Object классы
│   ├── base_page.py             # Базовый класс для всех страниц
│   ├── login_page.py            # Страница входа и регистрации
│   ├── signup_page.py           # Форма создания аккаунта
│   ├── products_page.py         # Каталог товаров и поиск
│   ├── checkout_page.py         # Оформление заказа
│   └── ...
├── tests/                       # Автотесты
│   ├── test_auth.py             # Авторизация и негативные сценарии
│   ├── test_products.py         # Каталог и DDT-поиск
│   ├── test_checkout.py         # E2E-сценарий покупки
│   └── ...
├── utils/                       # Вспомогательные утилиты
│   └── data_generator.py        # Генератор тестовых данных (Faker)
├── .gitignore
├── pytest.ini                   # Конфигурация Pytest
├── requirements.txt             # Зависимости проекта
└── README.md
```

---

## 🚀 Локальный запуск

### 1. Клонирование репозитория и установка зависимостей
```bash
git clone [https://github.com/CODE-DENYA/automation-exercise-tests.git](https://github.com/CODE-DENYA/automation-exercise-tests.git)
cd automation-exercise-tests

python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate

pip install -r requirements.txt
npx playwright install chromium
```

### 2. Запуск тестов
* **Запуск всех тестов:**
  ```bash
  pytest
  ```
* **Запуск с генерацией Allure-результатов:**
  ```bash
  pytest --alluredir=allure-results
  ```
* **Просмотр Allure-отчета локально:**
  ```bash
  allure serve allure-results
  ```
* **Запуск проверки качества кода (Ruff):**
  ```bash
  ruff check .
  ```

---

## 🔄 CI/CD Пайплайн

При каждом push или pull request в ветку `main` в GitHub Actions автоматически запускается Workflow:
1. Проводится проверка стиля кода с помощью **Ruff**.
2. Запускаются UI-тесты в headless-режиме с помощью Playwright.
3. Формируется и публикуется интерактивный отчет **Allure Report** на GitHub Pages.