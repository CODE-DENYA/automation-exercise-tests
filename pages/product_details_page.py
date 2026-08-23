import allure
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, page: Page, base_url: str = ""):
        super().__init__(page, base_url)

        self.view_product_btn: Locator = page.locator("a[href^='/product_details/']").first
        self.product_name: Locator = page.locator(".product-information h2")
        self.product_category: Locator = page.locator(".product-information p:has-text('Category')")
        self.product_price: Locator = page.locator(".product-information span span")
        self.product_availability: Locator = page.locator(".product-information p:has-text('Availability')")

    @allure.step("Перейти в карточку первого товара")
    def open_first_product_details(self):
        self.navigate("/products")
        self.view_product_btn.click()

    @allure.step("Получить данные о товаре")
    def get_product_details(self) -> dict:
        return {
            "name": self.product_name.inner_text(),
            "category_visible": self.product_category.is_visible(),
            "price": self.product_price.inner_text(),
            "availability_visible": self.product_availability.is_visible(),
        }