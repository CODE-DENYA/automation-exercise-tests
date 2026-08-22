import os
import allure
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://automationexercise.com")


@pytest.fixture(autouse=True)
def block_ads(page):
    # Блокируем рекламные сервисы и Google Vignette, блокирующие элементы
    page.route("**/*google*", lambda route: route.abort())
    page.route("**/*doubleclick*", lambda route: route.abort())
    page.route("**/*adservice*", lambda route: route.abort())


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, page):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            page.screenshot(full_page=True),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )