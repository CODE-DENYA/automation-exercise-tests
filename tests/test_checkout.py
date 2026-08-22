import allure
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from utils.data_generator import generate_user_data, generate_card_data


@allure.feature("Оформление заказа")
@allure.story("Полный E2E-сценарий покупки товара")
def test_full_checkout_flow(page, base_url):
    user_data = generate_user_data()
    card_data = generate_card_data()

    login_page = LoginPage(page, base_url)
    signup_page = SignupPage(page, base_url)
    products_page = ProductsPage(page, base_url)
    checkout_page = CheckoutPage(page, base_url)

    # 1. Регистрация пользователя
    login_page.open_login_page()
    login_page.start_signup(user_data["name"], user_data["email"])
    signup_page.fill_signup_form(user_data)

    # 2. Добавление товара
    products_page.open_products_page()
    products_page.add_first_product_to_cart()

    # 3. Оформление и оплата
    checkout_page.proceed_to_checkout()
    checkout_page.place_order("Покупка через автотест с Faker")
    checkout_page.fill_payment_and_pay(card_data)

    # 4. Проверка
    assert checkout_page.get_order_placed_message() == "ORDER PLACED!"