import time
import allure
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


@allure.feature("Авторизация")
@allure.story("Успешный переход на страницу входа")
def test_open_login_page(page, base_url):
    login_page = LoginPage(page, base_url)
    login_page.open_login_page()
    assert "Automation Exercise - Signup / Login" in login_page.get_title()


@allure.feature("Авторизация")
@allure.story("Ошибка при вводе неверных данных")
def test_login_with_invalid_credentials(page, base_url):
    login_page = LoginPage(page, base_url)
    login_page.open_login_page()
    login_page.login("wrong_email@test.com", "invalid_password")

    assert "Your email or password is incorrect!" in login_page.get_login_error_message()


@allure.feature("Регистрация")
@allure.story("Успешная регистрация нового пользователя")
def test_successful_registration(page, base_url):
    unique_email = f"user_{int(time.time())}@test.com"
    user_data = {
        "password": "Password123!",
        "day": "15",
        "month": "5",
        "year": "1995",
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Main Street",
        "country": "United States",
        "state": "California",
        "city": "Los Angeles",
        "zipcode": "90001",
        "mobile_number": "+1234567890",
    }

    login_page = LoginPage(page, base_url)
    signup_page = SignupPage(page, base_url)

    login_page.open_login_page()
    login_page.start_signup("Test User", unique_email)

    signup_page.fill_signup_form(user_data)

    assert signup_page.get_account_created_message() == "ACCOUNT CREATED!"