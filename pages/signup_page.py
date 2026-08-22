from playwright.sync_api import Page, Locator
import allure
from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        # Данные аккаунта
        self.gender_mr_radio: Locator = page.locator("#id_gender1")
        self.password_input: Locator = page.locator("#password")
        self.days_select: Locator = page.locator("#days")
        self.months_select: Locator = page.locator("#months")
        self.years_select: Locator = page.locator("#years")

        # Адресные данные
        self.first_name_input: Locator = page.locator("#first_name")
        self.last_name_input: Locator = page.locator("#last_name")
        self.address_input: Locator = page.locator("#address1")
        self.country_select: Locator = page.locator("#country")
        self.state_input: Locator = page.locator("#state")
        self.city_input: Locator = page.locator("#city")
        self.zipcode_input: Locator = page.locator("#zipcode")
        self.mobile_number_input: Locator = page.locator("#mobile_number")

        # Кнопка отправки, подтверждение и кнопка продолжения
        self.create_account_btn: Locator = page.locator("button[data-qa='create-account']")
        self.account_created_title: Locator = page.locator("h2[data-qa='account-created']")
        self.continue_btn: Locator = page.locator("a[data-qa='continue-button']")

    @allure.step("Заполнить форму регистрации")
    def fill_signup_form(self, user_data: dict):
        self.gender_mr_radio.check()
        self.password_input.fill(user_data["password"])
        self.days_select.select_option(user_data["day"])
        self.months_select.select_option(user_data["month"])
        self.years_select.select_option(user_data["year"])

        self.first_name_input.fill(user_data["first_name"])
        self.last_name_input.fill(user_data["last_name"])
        self.address_input.fill(user_data["address"])
        self.country_select.select_option(user_data["country"])
        self.state_input.fill(user_data["state"])
        self.city_input.fill(user_data["city"])
        self.zipcode_input.fill(user_data["zipcode"])
        self.mobile_number_input.fill(user_data["mobile_number"])

        self.create_account_btn.click()

    @allure.step("Получить заголовок успешного создания аккаунта")
    def get_account_created_message(self) -> str:
        return self.account_created_title.inner_text()

    @allure.step("Нажать кнопку Continue после создания аккаунта")
    def click_continue(self):
        self.continue_btn.click()