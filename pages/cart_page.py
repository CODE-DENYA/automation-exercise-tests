from playwright.sync_api import Page, Locator
import allure
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.cart_items: Locator = page.locator("#cart_info_table tbody tr")
        self.product_names: Locator = page.locator(".cart_description h4 a")

    @allure.step("Перейти на страницу корзины")
    def open_cart_page(self):
        self.navigate("/view_cart")

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        return self.cart_items.count()

    @allure.step("Получить названия товаров в корзине")
    def get_product_names(self) -> list[str]:
        return self.product_names.all_text_contents()