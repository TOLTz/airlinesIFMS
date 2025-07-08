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
        self.departure_date = datetime.now()

    def confirm_arrival(self):
        self.arrival_date = datetime.now()

    def add_crewmate(self, crewmate):
        self.crews.update(crewmate)
                
    def add_passenger(self, passenger):
        self.passengers.update(passenger)
    
    def add_connection(self, conection:dict):
        self.connections.append(conection)
        
    def __str__(self):
        return (f'ID:{self.id}, Crews:{self.crews}, Passengers:{self.passengers}')