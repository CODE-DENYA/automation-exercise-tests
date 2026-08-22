from playwright.sync_api import Page, Locator
import allure
from pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.name_input: Locator = page.locator("input[data-qa='name']")
        self.email_input: Locator = page.locator("input[data-qa='email']")
        self.subject_input: Locator = page.locator("input[data-qa='subject']")
        self.message_input: Locator = page.locator("textarea[data-qa='message']")
        self.upload_file_input: Locator = page.locator("input[name='upload_file']")
        self.submit_btn: Locator = page.locator("input[data-qa='submit-button']")
        self.success_msg: Locator = page.locator(".status.alert-success")

    @allure.step("Перейти на страницу 'Contact Us'")
    def open_contact_page(self):
        self.navigate("/contact_us")

    @allure.step("Заполнить форму обратной связи")
    def fill_contact_form(
        self,
        name: str,
        email: str,
        subject: str,
        message: str,
        file_path: str = None,
    ):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)
        if file_path:
            self.upload_file_input.set_input_files(file_path)

    @allure.step("Отправить форму обратной связи")
    def submit_form(self):
        # Автоматически нажимаем 'OK' во всплывающем системном окне alert
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_btn.click()

    @allure.step("Получить текст успешной отправки")
    def get_success_message(self) -> str:
        return self.success_msg.inner_text()