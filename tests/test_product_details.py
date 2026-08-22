import allure
from pages.product_details_page import ProductDetailsPage


@allure.feature("Каталог товаров")
@allure.story("Проверка отображения информации в карточке товара")
def test_product_details_info(page, base_url):
    product_details_page = ProductDetailsPage(page, base_url)

    product_details_page.open_first_product_details()
    details = product_details_page.get_product_details()

    assert len(details["name"]) > 0
    assert details["category_visible"]
    assert "Rs." in details["price"]
    assert details["availability_visible"]