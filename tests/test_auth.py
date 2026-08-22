import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_user_data


@allure.feature("Авторизация")
@allure.story("Успешный переход на страницу входа")
def test_open_login_page(page: Page, login_page: LoginPage):
    login_page.open_login_page()
    expect(page).to_have_title("Automation Exercise - Signup / Login")


@allure.feature("Авторизация")
@allure.story("Ошибка при вводе неверных данных")
def test_login_with_invalid_credentials(login_page: LoginPage):
    login_page.open_login_page()
    login_page.login("wrong_email@test.com", "invalid_password")

    expect(login_page.login_error_msg).to_contain_text("Your email or password is incorrect!")


@allure.feature("Регистрация")
@allure.story("Успешная регистрация нового пользователя")
def test_successful_registration(login_page: LoginPage, signup_page: SignupPage):
    user_data = generate_user_data()

    login_page.open_login_page()
    login_page.start_signup(user_data["name"], user_data["email"])
    signup_page.fill_signup_form(user_data)

    expect(signup_page.account_created_title).to_have_text("ACCOUNT CREATED!", ignore_case=True)