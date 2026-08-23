import allure
from playwright.sync_api import expect

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage
from utils.data_generator import generate_card_data, generate_user_data


@allure.feature("Оформление заказа")
@allure.story("Полный E2E-сценарий покупки товара")
def test_full_checkout_flow(
    login_page: LoginPage,
    signup_page: SignupPage,
    products_page: ProductsPage,
    checkout_page: CheckoutPage,
):
    user_data = generate_user_data()
    card_data = generate_card_data()

    # 1. Регистрация пользователя
    login_page.open_login_page()
    login_page.start_signup(user_data["name"], user_data["email"])
    signup_page.fill_signup_form(user_data)
    
    # 2. Авторизация в сессии после создания аккаунта
    signup_page.click_continue()

    # 3. Добавление товара
    products_page.open_products_page()
    products_page.add_first_product_to_cart()

    # 4. Оформление и оплата
    checkout_page.proceed_to_checkout()
    checkout_page.place_order("Покупка через автотест с Faker")
    checkout_page.fill_payment_and_pay(card_data)

    # 5. Проверка
    expect(checkout_page.order_placed_title).to_have_text("ORDER PLACED!", ignore_case=True)