import allure
from playwright.sync_api import expect

from pages.contact_page import ContactPage


@allure.feature("Обратная связь")
@allure.story("Отправка формы Contact Us с прикреплением файла")
def test_contact_us_form(contact_page: ContactPage, tmp_path):
    # Создаем временный файл для прикрепления
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, Playwright!")

    contact_page.open_contact_page()
    contact_page.fill_contact_form(
        name="Test User",
        email="contact_test@test.com",
        subject="Запрос в поддержку",
        message="Тестовое сообщение для проверки загрузки файла.",
        file_path=str(test_file),
    )
    contact_page.submit_form()

    expect(contact_page.success_msg).to_contain_text(
        "Success! Your details have been submitted successfully."
    )