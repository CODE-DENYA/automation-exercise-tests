from playwright.sync_api import Page, Locator
import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        # Локаторы формы входа (Login)
        self.login_email_input: Locator = page.locator("input[data-qa='login-email']")
        self.login_password_input: Locator = page.locator("input[data-qa='login-password']")
        self.login_button: Locator = page.locator("button[data-qa='login-button']")
        self.login_error_msg: Locator = page.locator("form[action='/login'] p")

        # Локаторы формы регистрации (Signup)
        self.signup_name_input: Locator = page.locator("input[data-qa='signup-name']")
        self.signup_email_input: Locator = page.locator("input[data-qa='signup-email']")
        self.signup_button: Locator = page.locator("button[data-qa='signup-button']")

    @allure.step("Перейти на страницу входа/регистрации")
    def open_login_page(self):
        self.navigate("/login")

    @allure.step("Выполнить вход с email: {email}")
    def login(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    @allure.step("Запустить регистрацию пользователя: {name}, email: {email}")
    def start_signup(self, name: str, email: str):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()
        self.page.wait_for_url("**/signup*")

    @allure.step("Получить текст ошибки авторизации")
    def get_login_error_message(self) -> str:
        return self.login_error_msg.inner_text()