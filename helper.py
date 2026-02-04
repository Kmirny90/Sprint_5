from faker import Faker

faker = Faker()

def generate_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=6)
    short_password = faker.password(length=5)
    return name, email, password, short_password