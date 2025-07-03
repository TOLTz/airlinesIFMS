from flight import Flight
from plane import *
from passenger import Passenger
from pilot import Pilot
from steward import Steward
from crew import CrewType
import random
from utils import *


if __name__ == '__main__':
    
    list_models = list(Models)
    
    names = random.sample(list_models, 10)
    airplanes = []
    for name in names:
        airplane_obj = Plane(name.value, Scope.GLOBAL.value)
        airplane_obj = airplane_obj.to_dict()
        airplanes.append(airplane_obj)
    
    for airplane in airplanes:
        input('continuar? ')
        pilot_name = generate_name()
        pilot_birthday = generate_birthday()
        pilot_cpf = generate_cpf()
        pilot_cht = generate_code()
        pilot = Pilot(pilot_name, pilot_birthday, pilot_cpf, CrewType.PILOT, pilot_cht).to_dict()

        copilot_name = generate_name()
        copilot_birthday = generate_birthday()
        copilot_cpf = generate_cpf()
        copilot_cht = generate_code()
        copilot = Pilot(copilot_name, copilot_birthday, copilot_cpf, CrewType.COPILOT, copilot_cht).to_dict()

        stewards = []
        for _ in range(5):
            steward_name = generate_name()
            steward_birthday = generate_birthday()
            steward_cpf = generate_cpf()
            steward_cms = generate_code(prefix='CMS')
            steward = Steward(steward_name, steward_birthday, steward_cpf, CrewType.STEWARD, steward_cms).to_dict()
            stewards.append(steward)
            
        crewmates = {'Pilot': pilot, 'Copilot':copilot, 'Stewards':stewards}
        
        
        passengers = {}
        for seat in range(250):
            seat += 1
            passenger_name = generate_name()
            passenger_birthday = generate_birthday()
            passenger_cpf = generate_cpf()
            passenger_passport = generate_passport_number()
            loyalty_code = generate_loyalty_number()
            needs = random_bool()
            passenger = Passenger(passenger_name, passenger_birthday, passenger_cpf, passenger_passport, loyalty_code, needs).to_dict()
            passengers.update({seat : passenger})
    
        flight = Flight(airplane, 'Guarulhos', 'Paris', 5000)
        flight.add_crewmate(crewmate=crewmates)
        flight.add_passenger(passengers)
        

    