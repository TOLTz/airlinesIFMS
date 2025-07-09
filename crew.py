from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4
from enum import Enum

class CrewType(Enum):
    PILOT = 'Pilot'
    COPILOT = 'Copilot'
    STEWARD = 'Steward'

class Crew(ABC):
    def __init__(self, name, birthday, cpf, role):
        self._id = uuid4()
        self._name = name
        self._birthday = birthday
        self._cpf = cpf
        self._role = role 
        self._registerDate = datetime.now()

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if not isinstance(value, Enum):
            raise TypeError("Role deve ser uma instância de Enum.")
        self._role = value

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser uma string.")
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
        if not isinstance(value, str) or len(value) != 14:
            raise ValueError("CPF inválido. Deve estar no formato '000.000.000-00'")
        self._cpf = value

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
