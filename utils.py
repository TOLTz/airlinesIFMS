import random
from string import ascii_uppercase, digits
from faker import Faker


def generate_loyalty_number(length=8):
    valid_characters = ascii_uppercase + digits
    code = ''.join(random.choice(valid_characters) for _ in range(length))
    return code

def generate_passport_number():
    fake = Faker('pt_BR')
    passport = fake.passport_number()
    return passport

def random_bool():
    choice = random.choice([True, False])
    return choice

def generate_code(prefix="CHT-", length=8):
    valid_characters = ascii_uppercase + digits
    
    suffix = ''.join(random.choice(valid_characters) for _ in range(length))
    return f"{prefix}{suffix}"

def generate_name():
    fake = Faker('pt_BR')
    return fake.name()

def generate_birthday():
    fake = Faker('pt_BR')
    return fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y')

def generate_cpf():
    fake = Faker('pt_BR')
    return fake.cpf()