import time
import allure
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


@allure.feature("Оформление заказа")
@allure.story("Полный E2E-сценарий покупки товара")
def test_full_checkout_flow(page, base_url):
    unique_email = f"buyer_{int(time.time())}@test.com"
    user_data = {
        "password": "Password123!",
        "day": "10",
        "month": "1",
        "year": "1990",
        "first_name": "John",
        "last_name": "Doe",
        "address": "456 Test Street",
        "country": "United States",
        "state": "Texas",
        "city": "Austin",
        "zipcode": "78701",
        "mobile_number": "+19998887766",
    }
    card_data = {
        "name": "John Doe",
        "card_number": "4111111111111111",
        "cvc": "123",
        "month": "12",
        "year": "2028",
    }

    login_page = LoginPage(page, base_url)
    signup_page = SignupPage(page, base_url)
    products_page = ProductsPage(page, base_url)
    checkout_page = CheckoutPage(page, base_url)

    # 1. Регистрация пользователя
    login_page.open_login_page()
    login_page.start_signup("John Doe", unique_email)
    signup_page.fill_signup_form(user_data)

    # 2. Добавление товара
    products_page.open_products_page()
    products_page.add_first_product_to_cart()

    # 3. Оформление и оплата
    checkout_page.proceed_to_checkout()
    checkout_page.place_order("Покупка через автотест")
    checkout_page.fill_payment_and_pay(card_data)

    # 4. Проверка
    assert checkout_page.get_order_placed_message() == "ORDER PLACED!"