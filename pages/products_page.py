from playwright.sync_api import Page, Locator
import allure
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.search_input: Locator = page.locator("#search_product")
        self.search_button: Locator = page.locator("#submit_search")
        self.searched_title: Locator = page.locator("h2.title.text-center")
        self.product_items: Locator = page.locator(".product-image-wrapper")

    @allure.step("Перейти на страницу каталога товаров")
    def open_products_page(self):
        self.navigate("/products")

    @allure.step("Выполнить поиск по ключевому слову: {keyword}")
    def search_product(self, keyword: str):
        self.search_input.fill(keyword)
        self.search_button.click()

    @allure.step("Получить количество отображаемых товаров")
    def get_products_count(self) -> int:
        return self.product_items.count()

    @allure.step("Получить заголовок страницы поиска")
    def get_searched_title_text(self) -> str:
        return self.searched_title.inner_text()