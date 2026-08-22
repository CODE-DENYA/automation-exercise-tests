import allure
from pages.base_page import BasePage
from utils.data_generator import generate_user_data


@allure.feature("Футер")
@allure.story("Подписка на рассылку новостей")
def test_newsletter_subscription(page, base_url):
    user_data = generate_user_data()
    base_page = BasePage(page, base_url)

    base_page.navigate("/")
    base_page.subscribe_to_newsletter(user_data["email"])

    assert "You have been successfully subscribed!" in base_page.get_subscription_success_message()