import allure
from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage


@allure.feature("Каталог товаров")
@allure.story("Открытие каталога")
def test_open_products_page(page: Page, products_page: ProductsPage):
    products_page.open_products_page()

    expect(page).to_have_title("Automation Exercise - All Products")
    expect(products_page.product_items.first).to_be_visible()


@allure.feature("Каталог товаров")
@allure.story("Поиск товара через поисковую строку")
def test_search_product(products_page: ProductsPage):
    products_page.open_products_page()
    products_page.search_product("dress")

    expect(products_page.searched_title).to_have_text("SEARCHED PRODUCTS", ignore_case=True)
    expect(products_page.product_items.first).to_be_visible()