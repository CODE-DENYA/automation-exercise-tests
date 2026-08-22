from playwright.sync_api import Page
import allure

class BasePage:
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url

    @allure.step("Закрыть баннер согласия с cookie/GDPR")
    def handle_consent_banner(self):
        consent_button = self.page.locator(".fc-consent-root .fc-cta-consent")
        try:
            if consent_button.is_visible(timeout=3000):
                consent_button.click()
        except Exception:
            pass

    @allure.step("Открыть страницу: {path}")
    def navigate(self, path: str = ""):
        target_url = f"{self.base_url}{path}" if self.base_url else path
        self.page.goto(target_url)
        self.handle_consent_banner()

    @allure.step("Получить заголовок страницы")
    def get_title(self) -> str:
        return self.page.title()