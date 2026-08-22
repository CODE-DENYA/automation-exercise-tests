import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from utils.data_generator import generate_user_data


@allure.feature("Футер")
@allure.story("Подписка на рассылку новостей")
def test_newsletter_subscription(base_page: BasePage):
    user_data = generate_user_data()

    base_page.navigate("/")
    base_page.subscribe_to_newsletter(user_data["email"])

    expect(base_page.success_subscribe_msg).to_contain_text(
        "You have been successfully subscribed!"
    )