from playwright.sync_api import Page, Locator
import allure
from pages.base_page import BasePage


class DeleteAccountPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.delete_account_btn: Locator = page.locator("a[href='/delete_account']")
        self.account_deleted_title: Locator = page.locator("h2[data-qa='account-deleted']")

    @allure.step("Удалить аккаунт")
    def click_delete_account(self):
        self.delete_account_btn.click()

    @allure.step("Получить подтверждение удаления аккаунта")
    def get_account_deleted_message(self) -> str:
        return self.account_deleted_title.inner_text()