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

def generate_flight_info(scope):
    nacional = ['Guarulhos', 'Congonhas', 'Brasília', 'Galeão', 'Salvador', 'Porto Alegre', 'Recife']
    internacional = ['Buenos Aires', 'Santiago', 'Lima', 'Montevidéu', 'Cidade do Panamá']
    global_ = ['Nova York', 'Paris', 'Londres', 'Tóquio', 'Lisboa', 'Dubai', 'Toronto']

    all_dests = {
        'nacional': (nacional, nacional, (300, 800)),
        'internacional': (nacional, internacional, (900, 2500)),
        'global': (nacional + internacional, global_, (3000, 9000))
    }

    origem_list, destino_list, price_range = all_dests[scope.lower()]

    origin = random.choice(origem_list)
    destination = random.choice([d for d in destino_list if d != origin])

    price = round(random.uniform(*price_range), 2)
    flight_code = ''.join(random.choices(f'{ascii_uppercase + digits}', k=5))

    return origin, destination, price, flight_code
