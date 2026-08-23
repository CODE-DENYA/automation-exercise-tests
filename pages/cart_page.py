import allure
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.cart_items: Locator = page.locator("#cart_info_table tbody tr")
        self.product_names: Locator = page.locator(".cart_description h4 a")
        self.delete_btn: Locator = page.locator(".cart_quantity_delete").first
        self.empty_cart_msg: Locator = page.locator("#empty_cart")

    @allure.step("Перейти на страницу корзины")
    def open_cart_page(self):
        self.navigate("/view_cart")

    @allure.step("Удалить первый товар из корзины")
    def delete_first_product(self):
        self.delete_btn.click()

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        return self.cart_items.count()

    @allure.step("Получить названия товаров в корзине")
    def get_product_names(self) -> list[str]:
        return self.product_names.all_text_contents()

    @allure.step("Проверить, отображается ли сообщение о пустой корзине")
    def is_cart_empty(self) -> bool:
        return self.empty_cart_msg.is_visible()