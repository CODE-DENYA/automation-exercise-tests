import allure
from playwright.sync_api import Error, Locator, Page


class BasePage:
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url

        # Локаторы подписки в футере
        self.subscription_email_input: Locator = page.locator("#susbscribe_email")
        self.subscribe_btn: Locator = page.locator("#subscribe")
        self.success_subscribe_msg: Locator = page.locator(".alert-success")

    @allure.step("Закрыть баннер согласия с cookie/GDPR")
    def handle_consent_banner(self):
        consent_button = self.page.locator(".fc-consent-root .fc-cta-consent")
        try:
            if consent_button.is_visible(timeout=3000):
                consent_button.click()
        except Error:
            pass

    @allure.step("Открыть страницу: {path}")
    def navigate(self, path: str = ""):
        target_url = f"{self.base_url}{path}" if self.base_url else path
        self.page.goto(target_url)
        self.handle_consent_banner()

    @allure.step("Получить заголовок страницы")
    def get_title(self) -> str:
        return self.page.title()

    @allure.step("Подписаться на рассылку в футере: {email}")
    def subscribe_to_newsletter(self, email: str):
        self.subscription_email_input.fill(email)
        self.subscribe_btn.click()

    @allure.step("Получить текст успешной подписки")
    def get_subscription_success_message(self) -> str:
        return self.success_subscribe_msg.inner_text()