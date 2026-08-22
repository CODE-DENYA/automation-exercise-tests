import allure
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.delete_account_page import DeleteAccountPage
from utils.data_generator import generate_user_data


@allure.feature("Управление аккаунтом")
@allure.story("Успешное удаление аккаунта пользователя")
def test_delete_account(page, base_url):
    user_data = generate_user_data()

    login_page = LoginPage(page, base_url)
    signup_page = SignupPage(page, base_url)
    delete_account_page = DeleteAccountPage(page, base_url)

    # 1. Регистрация нового пользователя
    login_page.open_login_page()
    login_page.start_signup(user_data["name"], user_data["email"])
    signup_page.fill_signup_form(user_data)

    assert signup_page.get_account_created_message().upper() == "ACCOUNT CREATED!"

    # 2. Переход в систему
    signup_page.click_continue()

    # 3. Удаление аккаунта
    delete_account_page.click_delete_account()

    # 4. Проверка сообщения об удалении
    assert delete_account_page.get_account_deleted_message().upper() == "ACCOUNT DELETED!"