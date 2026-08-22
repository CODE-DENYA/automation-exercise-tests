import allure
from pages.contact_page import ContactPage


@allure.feature("Обратная связь")
@allure.story("Отправка формы Contact Us с прикреплением файла")
def test_contact_us_form(page, base_url, tmp_path):
    # Создаем временный файл для прикрепления
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, Playwright!")

    contact_page = ContactPage(page, base_url)
    contact_page.open_contact_page()

    contact_page.fill_contact_form(
        name="Test User",
        email="contact_test@test.com",
        subject="Запрос в поддержку",
        message="Тестовое сообщение для проверки загрузки файла.",
        file_path=str(test_file),
    )
    contact_page.submit_form()

    assert (
        "Success! Your details have been submitted successfully."
        in contact_page.get_success_message()
    )