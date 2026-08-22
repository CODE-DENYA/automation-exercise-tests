from playwright.sync_api import Page, Locator
import allure
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.proceed_to_checkout_btn: Locator = page.locator(".check_out")
        self.comment_textarea: Locator = page.locator("textarea[name='message']")
        self.place_order_btn: Locator = page.locator("a[href='/payment']")

        # Поля оплаты
        self.name_on_card: Locator = page.locator("input[data-qa='name-on-card']")
        self.card_number: Locator = page.locator("input[data-qa='card-number']")
        self.cvc: Locator = page.locator("input[data-qa='cvc']")
        self.exp_month: Locator = page.locator("input[data-qa='expiry-month']")
        self.exp_year: Locator = page.locator("input[data-qa='expiry-year']")
        self.pay_btn: Locator = page.locator("button[data-qa='pay-button']")

        # Подтверждение
        self.order_placed_title: Locator = page.locator("h2[data-qa='order-placed']")

    @allure.step("Перейти к оформлению заказа из корзины")
    def proceed_to_checkout(self):
        self.proceed_to_checkout_btn.click()

    @allure.step("Подтвердить заказ и перейти к оплате")
    def place_order(self, comment: str = "Тестовый заказ"):
        self.comment_textarea.fill(comment)
        self.place_order_btn.click()

    @allure.step("Заполнить платежные данные и оплатить")
    def fill_payment_and_pay(self, card_data: dict):
        self.name_on_card.fill(card_data["name"])
        self.card_number.fill(card_data["card_number"])
        self.cvc.fill(card_data["cvc"])
        self.exp_month.fill(card_data["month"])
        self.exp_year.fill(card_data["year"])
        self.pay_btn.click()

    @allure.step("Получить сообщение об успешном оформлении")
    def get_order_placed_message(self) -> str:
        return self.order_placed_title.inner_text()