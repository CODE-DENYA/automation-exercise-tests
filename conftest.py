import os

import allure
import pytest
from dotenv import load_dotenv

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.contact_page import ContactPage
from pages.delete_account_page import DeleteAccountPage
from pages.login_page import LoginPage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://automationexercise.com")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": ["--disable-blink-features=AutomationControlled"],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/128.0.0.0 Safari/537.36"
        ),
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(autouse=True)
def block_ads(page):
    ad_domains = [
        "**/*googlesyndication.com/**",
        "**/*doubleclick.net/**",
        "**/*adservice.google.com/**",
        "**/*pagead2.googlesyndication.com/**",
    ]
    for domain in ad_domains:
        page.route(domain, lambda route: route.abort())


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def attach_artifacts_on_failure(request, page, context):
    # Включаем трассировку для каждого теста
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    # При падении прикрепляем скриншот и Trace zip
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            page.screenshot(full_page=True),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
        trace_path = f"allure-results/trace_{request.node.name}.zip"
        context.tracing.stop(path=trace_path)
        allure.attach.file(
            trace_path,
            name="playwright_trace",
            extension="zip",
        )
    else:
        context.tracing.stop()


# --- Фикстуры для Page Objects ---

@pytest.fixture
def base_page(page, base_url):
    return BasePage(page, base_url)


@pytest.fixture
def login_page(page, base_url):
    return LoginPage(page, base_url)


@pytest.fixture
def signup_page(page, base_url):
    return SignupPage(page, base_url)


@pytest.fixture
def products_page(page, base_url):
    return ProductsPage(page, base_url)


@pytest.fixture
def product_details_page(page, base_url):
    return ProductDetailsPage(page, base_url)


@pytest.fixture
def cart_page(page, base_url):
    return CartPage(page, base_url)


@pytest.fixture
def checkout_page(page, base_url):
    return CheckoutPage(page, base_url)


@pytest.fixture
def contact_page(page, base_url):
    return ContactPage(page, base_url)


@pytest.fixture
def delete_account_page(page, base_url):
    return DeleteAccountPage(page, base_url)