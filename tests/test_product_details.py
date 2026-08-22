import allure
from playwright.sync_api import expect
from pages.product_details_page import ProductDetailsPage


@allure.feature("Каталог товаров")
@allure.story("Проверка отображения информации в карточке товара")
def test_product_details_info(product_details_page: ProductDetailsPage):
    product_details_page.open_first_product_details()

    expect(product_details_page.product_name).not_to_be_empty()
    expect(product_details_page.product_category).to_be_visible()
    expect(product_details_page.product_price).to_contain_text("Rs.")
    expect(product_details_page.product_availability).to_be_visible()