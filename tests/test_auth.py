import allure
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_user_data


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
    user_data = generate_user_data()

    login_page = LoginPage(page, base_url)
    signup_page = SignupPage(page, base_url)

    login_page.open_login_page()
    login_page.start_signup(user_data["name"], user_data["email"])

    signup_page.fill_signup_form(user_data)

    assert signup_page.get_account_created_message() == "ACCOUNT CREATED!"