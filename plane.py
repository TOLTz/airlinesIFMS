from uuid import uuid4
from enum import Enum


class Models(Enum):
    BOEING_737 = "Boeing 737"
    AIRBUS_A320 = "Airbus A320"
    EMBRAER_E195 = "Embraer E195"
    CESSNA_172 = "Cessna 172"
    BOMBARDIER_Q400 = "Bombardier Q400"
    BOEING_747 = "Boeing 747"
    AIRBUS_A380 = "Airbus A380"
    LOCKHEED_C130_HERCULES = "Lockheed C-130 Hercules"
    DOUGLAS_DC3 = "Douglas DC-3"
    F16_FIGHTING_FALCON = "F-16 Fighting Falcon"
    ATR_72 = "ATR 72"
    PILATUS_PC12 = "Pilatus PC-12"

class Scope(Enum):
    NACIONAL = 'nacional'
    INTERNACIONAL = 'internacional'
    GLOBAL = 'global'

class Plane:
    def __init__(self, model, reach, max_seat = 250):
        self._id = uuid4()
        self._model = model
        self._reach = reach
        self._max_seat = max_seat

    @property
    def max_seat(self):
        return self._max_seat

    @max_seat.setter
    def max_seat(self, value):
        self._max_seat = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def reach(self):
        return self._reach

    @reach.setter
    def reach(self, value):
        if isinstance(value, Enum):
            self._reach = value


    def to_dict(self):
        
        """
            Função que transforma o objeto em dicionario
        Returns:
            dict: dicionario com as informações
        """
        return {
            'ID':     self.id,
            'Model':  self.model,
            'Alcance':self.reach,
            'Lugares':self.max_seat
        }

    def __str__(self) -> str:
        return f'ID: {self.id}, modelo: {self.model}, Alcance: {self.reach}' 

    