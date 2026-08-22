import allure
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@allure.feature("Корзина")
@allure.story("Добавление товара в корзину из каталога")
def test_add_product_to_cart(page, base_url):
    products_page = ProductsPage(page, base_url)
    cart_page = CartPage(page, base_url)

    products_page.open_products_page()
    products_page.add_first_product_to_cart()

    assert cart_page.get_cart_items_count() > 0
    assert len(cart_page.get_product_names()) > 0


@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
def test_delete_product_from_cart(page, base_url):
    products_page = ProductsPage(page, base_url)
    cart_page = CartPage(page, base_url)

    products_page.open_products_page()
    products_page.add_first_product_to_cart()

    cart_page.delete_first_product()

    page.wait_for_timeout(1000)
    assert cart_page.is_cart_empty() or cart_page.get_cart_items_count() == 0