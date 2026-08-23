import allure
from playwright.sync_api import expect

from pages.delete_account_page import DeleteAccountPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_user_data


@allure.feature("Управление аккаунтом")
@allure.story("Успешное удаление аккаунта пользователя")
def test_delete_account(
    login_page: LoginPage,
    signup_page: SignupPage,
    delete_account_page: DeleteAccountPage,
):
    user_data = generate_user_data()

    # 1. Регистрация нового пользователя
    login_page.open_login_page()
    login_page.start_signup(user_data["name"], user_data["email"])
    signup_page.fill_signup_form(user_data)

    expect(signup_page.account_created_title).to_have_text("ACCOUNT CREATED!", ignore_case=True)

    # 2. Переход в систему
    signup_page.click_continue()

    # 3. Удаление аккаунта
    delete_account_page.click_delete_account()

    # 4. Проверка сообщения об удалении
    expect(delete_account_page.account_deleted_title).to_have_text("ACCOUNT DELETED!", ignore_case=True)