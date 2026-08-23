import allure
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.search_input: Locator = page.locator("#search_product")
        self.search_button: Locator = page.locator("#submit_search")
        self.searched_title: Locator = page.locator("h2.title.text-center")
        self.product_items: Locator = page.locator(".product-image-wrapper")
        self.add_to_cart_btn: Locator = page.locator(".add-to-cart").first
        self.view_cart_link: Locator = page.locator("u:has-text('View Cart')")

    @allure.step("Перейти на страницу каталога товаров")
    def open_products_page(self):
        self.navigate("/products")

    @allure.step("Выполнить поиск по ключевому слову: {keyword}")
    def search_product(self, keyword: str):
        self.search_input.fill(keyword)
        self.search_button.click()

    @allure.step("Добавить первый товар в корзину и перейти в корзину")
    def add_first_product_to_cart(self):
        self.product_items.first.hover()
        self.add_to_cart_btn.click()
        self.view_cart_link.click()

    @allure.step("Получить количество отображаемых товаров")
    def get_products_count(self) -> int:
        return self.product_items.count()

    @allure.step("Получить заголовок страницы поиска")
    def get_searched_title_text(self) -> str:
        return self.searched_title.inner_text()