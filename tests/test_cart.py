import allure
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.products_page import ProductsPage


@allure.feature("Корзина")
@allure.story("Добавление товара в корзину из каталога")
def test_add_product_to_cart(products_page: ProductsPage, cart_page: CartPage):
    products_page.open_products_page()
    products_page.add_first_product_to_cart()

    expect(cart_page.cart_items.first).to_be_visible()
    expect(cart_page.product_names.first).not_to_be_empty()


@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
def test_delete_product_from_cart(products_page: ProductsPage, cart_page: CartPage):
    products_page.open_products_page()
    products_page.add_first_product_to_cart()

    cart_page.delete_first_product()

    # Больше никаких page.wait_for_timeout! Playwright автоматически подождет исчезновения элемента или появления пустой корзины
    expect(cart_page.cart_items).to_have_count(0)