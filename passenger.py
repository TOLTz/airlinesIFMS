from uuid import uuid4
from datetime import datetime


class Passenger:
    def __init__(self, name, birthday, cpf, passaport_number, loyalty_program_number, special_needs):
        self._id = uuid4()
        self._name = name
        self._birthday = birthday
        self._cpf = cpf
        self._passport_number = passaport_number
        self._loyalty_program_number =loyalty_program_number
        self._special_needs = special_needs
        self._cration_date = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def cration_date(self):
        return self._cration_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def passport_number(self):
        return self._passport_number

    @passport_number.setter
    def passport_number(self, value):
        self._passport_number = value

    @property
    def loyalty_program_number(self):
        return self._loyalty_program_number

    @loyalty_program_number.setter
    def loyalty_program_number(self, value):
        self._loyalty_program_number = value

    @property
    def special_needs(self):
        return self._special_needs

    @special_needs.setter
    def special_needs(self, value):
        self._special_needs = value


    def to_dict(self):
        return {
            'id': str(self.id), # Converte UUID para string
            'name': self.name,
            'birthday': self.birthday, # Considere formatar para string se necessário
            'cpf': self.cpf,
            'passport_number': self.passport_number,
            'loyalty_program_number': self.loyalty_program_number,
            'special_needs': self.special_needs,
            'creation_date': self._cration_date.isoformat() # Formata a data para ISO 8601 string
        }


    def __str__(self):
        return (f'Nome:{self._name}, Data de nascimento: {self.birthday}'
                f'CPF:{self.cpf}, Numero do passaporte: {self.passport_number}'
                f'Numero do programa de fidelidade: {self.loyalty_program_number}'
                f'Necessidades especiais: {self.special_needs}')
        
        
        