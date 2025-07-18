from uuid import uuid4
from plane import Plane
import random
from datetime import datetime

class Flight:
    def __init__(self, plane:Plane, origin:str, destination:str, price:float):
        self._id = uuid4()
        self._crews = {}
        self._plane = plane
        self._departure_date = datetime.min
        self._arrival_date = datetime.min
        self._passengers = {}
        self._origin = origin
        self._connections = []
        self._destination = destination
        self.price = price
    @property
    def id(self):
        return self._id

    @property
    def crews(self):
        return self._crews

    @property
    def plane(self):
        return self._plane

    @plane.setter
    def plane(self, value):
        self._plane = value

    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, value):
        self._departure_date = value

    @property
    def arrival_date(self):
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, value):
        self._arrival_date = value

    @property
    def passengers(self):
        return self._passengers

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, value):
        self._connections = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    def liberate_plane(self):
        """
        Função que libera o avião e salva a data de liberação
        """
        self.departure_date = datetime.now()

    def confirm_arrival(self):
        """
        Função que confirma a chegada do avião e salva sua data
        """
        self.arrival_date = datetime.now()

    def add_crewmate(self, crewmate):
        """
        Função para adicionar novos tripulantes ao voo

        Args:
            crewmate (dict): Dicionarios com as informações dos tripulantes.
        """
        try:
            if not isinstance(crewmate, dict):
                raise TypeError("Crewmate precisa ser um dicionário.")
            self.crews.update(crewmate)
        except Exception as e:
            print(f"Erro ao adicionar tripulação: {e}")
                
    def add_passenger(self, passenger):
        """
        Função para adicionar novo passageiro ao voo

        Args:
            passenger (dict): Dicionario com as info do tripulante
        """
        try:
            for seat, p in passenger.items():
                if seat in self._passengers:
                    raise ValueError(f"Assento {seat} já está ocupado.")
                if not isinstance(p, dict) or "name" not in p:
                    raise TypeError("Dados do passageiro inválidos.")
            self.passengers.update(passenger)
        except Exception as e:
            print(f"Erro ao adicionar passageiro: {e}")

    
    def add_connection(self, conection:dict):
        """_summary_

        Args:
            conection (dict): Dicionario com as conexões feitas até a conclusão do voo
        """
        try:
            if not isinstance(conection, dict) or "stop" not in conection:
                raise ValueError("Conexão inválida. Precisa conter a chave 'stop'.")
            self.connections.append(conection)
        except Exception as e:
            print(f"Erro ao adicionar conexão: {e}")
        
    def __str__(self):
        return (f'ID:{self.id}, Crews:{self.crews}, Passengers:{self.passengers}')