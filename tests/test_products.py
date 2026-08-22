import allure
from pages.products_page import ProductsPage


@allure.feature("Каталог товаров")
@allure.story("Открытие каталога")
def test_open_products_page(page, base_url):
    products_page = ProductsPage(page, base_url)
    products_page.open_products_page()

    assert "Automation Exercise - All Products" in products_page.get_title()
    assert products_page.get_products_count() > 0


@allure.feature("Каталог товаров")
@allure.story("Поиск товара через поисковую строку")
def test_search_product(page, base_url):
    products_page = ProductsPage(page, base_url)
    products_page.open_products_page()

    products_page.search_product("dress")

    assert "SEARCHED PRODUCTS" in products_page.get_searched_title_text()
    assert products_page.get_products_count() > 0