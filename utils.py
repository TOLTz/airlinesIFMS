import random
from string import ascii_uppercase, digits
from faker import Faker


def generate_loyalty_number(length=8):
    """
    Função que gera um numero para o programa de fidelidade

    Args:
        length (int, optional): Caso quiser modificar o numero de caracteres. Defaults to 8.

    Returns:
        str: Retorna um str com o numero do programa de fidelidade
    """
    valid_characters = ascii_uppercase + digits
    code = ''.join(random.choice(valid_characters) for _ in range(length))
    return code

def generate_passport_number():
    """
    Função que gera um numero de passaporte aleatório
    Returns:
        str: numero falso gerado pelo faker
    """
    fake = Faker('pt_BR')
    passport = fake.passport_number()
    return passport

def random_bool():
    """
    Função que escolhe aleatóriamente um bool

    Returns:
        boll: True or False
    """
    choice = random.choice([True, False])
    return choice

def generate_code(prefix="CHT-", length=8):
    """
    Gera um código de CHT(para piloto) ou CMT(para comissario de bordo) para 

    Args:
        prefix (str, optional): Prefixo do documento. Defaults to "CHT-".
        length (int, optional): quantidade de caracteres no documento. Defaults to 8.

    Returns:
        str: retorna um str com o documento
    """
    valid_characters = ascii_uppercase + digits
    
    suffix = ''.join(random.choice(valid_characters) for _ in range(length))
    return f"{prefix}{suffix}"

def generate_name():
    """
    Gera um nome falso

    Returns:
        str: Retorna um nome falso em str
    """
    fake = Faker('pt_BR')
    return fake.name()

def generate_birthday():
    """
    Gera uma data de aniversario falsa com idade minima de 18 e maxima de 60

    Returns:
        str: retorna um str com a data de aniversario
    """
    fake = Faker('pt_BR')
    return fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y')

def generate_cpf():
    """
    Gera um CPF falso

    Returns:
        str: retorna um cpf falso
    """
    fake = Faker('pt_BR')
    return fake.cpf()

def generate_flight_info(scope):
    """
    Função que gera dados do voo, como origem, destino, preço e
    codigo de voo de acordo com o destino

    Args:
        scope (str): utiliza o value de um ENUM, para identificar o escopo do avião e assim colocar as informações

    Returns:
        str: retorna as informações do voo 
    """
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
