import uuid

from faker import Faker

fake = Faker("en_US")


def generate_user_data() -> dict:
    # Генерируем уникальный суффикс через uuid, чтобы email гарантированно не повторялся
    unique_id = uuid.uuid4().hex[:8]

    return {
        "name": fake.name(),
        "email": f"test_{unique_id}_{fake.email()}",
        "password": fake.password(length=12),
        "day": str(fake.random_int(min=1, max=28)),
        "month": str(fake.random_int(min=1, max=12)),
        "year": str(fake.random_int(min=1970, max=2000)),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number(),
    }


def generate_card_data() -> dict:
    return {
        "name": fake.name(),
        "card_number": fake.credit_card_number(card_type="visa"),
        "cvc": fake.credit_card_security_code(),
        "month": "12",
        "year": "2028",
    }